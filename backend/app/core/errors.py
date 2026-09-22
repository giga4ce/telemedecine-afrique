"""Centralized error handling (SPEC-03).

All handlers return a consistent JSON envelope `{"error": {"code", "message"}}`
and never leak stack traces or internal technical details to the client.
Unexpected exceptions are logged server-side and answered with a generic 500.

Public vs internal message (revue KAN-6 — bloquant 1)
----------------------------------------------------
The raw ``detail`` of an ``HTTPException`` is treated as INTERNAL and is never
returned to the client by default: a detail may carry a file path, an upstream
error or business context that must not leak. Instead the client receives a
generic message derived from the HTTP status code (e.g. "Not Found" for 404).
A route that wants a specific, curated client-facing message must raise
``PublicHTTPException(public_message=...)`` — an explicit opt-in. The internal
``detail`` still travels to the server logs, never to the response body.
"""

import logging
from http import HTTPStatus

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = logging.getLogger("app.errors")


class PublicHTTPException(HTTPException):
    """HTTPException whose ``public_message`` is safe to expose to the client.

    ``detail`` keeps its internal role (server logs); ``public_message`` is the
    only text the client-facing handler will render. Use this to opt in to a
    specific client message; otherwise a generic status message is returned.
    """

    def __init__(
        self,
        status_code: int,
        public_message: str,
        detail: object | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        self.public_message = public_message


def _error_body(code: int, message: str, **extra: object) -> dict[str, object]:
    body: dict[str, object] = {"error": {"code": code, "message": message}}
    if extra:
        body["error"].update(extra)  # type: ignore[union-attr]
    return body


def _public_message(exc: StarletteHTTPException) -> str:
    """Return a client-safe message.

    Only an explicit ``public_message`` (PublicHTTPException) is exposed; the
    raw ``detail`` is deliberately ignored. Fallback: the standard reason phrase
    for the status code, or a neutral "Error" for unknown codes.
    """
    explicit = getattr(exc, "public_message", None)
    if explicit:
        return str(explicit)
    try:
        return HTTPStatus(exc.status_code).phrase
    except ValueError:
        return "Error"


async def http_exception_handler(
    request: Request, exc: StarletteHTTPException
) -> JSONResponse:
    """Standardize HTTP errors into the envelope, without leaking ``detail``."""
    return JSONResponse(
        status_code=exc.status_code,
        content=_error_body(exc.status_code, _public_message(exc)),
    )


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """Return 422 with sanitized field errors (no raw input values echoed)."""
    fields = [
        {"loc": list(err.get("loc", [])), "msg": err.get("msg"), "type": err.get("type")}
        for err in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content=_error_body(422, "Validation error", fields=fields),
    )


async def unhandled_exception_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    """Log the real error server-side, answer a generic 500 with no internals.

    Vigilance (revue KAN-6 — amélioration 1) : ``logger.exception`` écrit le
    message ET la traceback complète de l'exception d'origine dans les logs
    serveur. Ces logs peuvent donc contenir des données internes — et, dès que
    des routes manipuleront des données DICOM/patient (SPEC-06+), potentiellement
    de la donnée sensible véhiculée par l'exception. À revoir avant tout usage
    hors POC : filtrage/scrubbing des logs, niveau et rétention. Le POC exclut
    la sécurité de production, donc on trace ici la vigilance sans corriger le
    pipeline de logs à ce stade. La RÉPONSE au client, elle, ne fuite rien.
    """
    logger.exception("Unhandled error on %s %s", request.method, request.url.path)
    return JSONResponse(
        status_code=500,
        content=_error_body(500, "Internal Server Error"),
    )


def register_error_handlers(app: FastAPI) -> None:
    """Wire the handlers onto the FastAPI application."""
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)
