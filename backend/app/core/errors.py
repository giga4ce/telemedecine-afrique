"""Centralized error handling (SPEC-03).

All handlers return a consistent JSON envelope `{"error": {"code", "message"}}`
and never leak stack traces or internal technical details to the client.
Unexpected exceptions are logged server-side and answered with a generic 500.
"""

import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = logging.getLogger("app.errors")


def _error_body(code: int, message: str, **extra: object) -> dict[str, object]:
    body: dict[str, object] = {"error": {"code": code, "message": message}}
    if extra:
        body["error"].update(extra)  # type: ignore[union-attr]
    return body


async def http_exception_handler(
    request: Request, exc: StarletteHTTPException
) -> JSONResponse:
    """Standardize HTTP errors (404, 405, explicit raises) into the envelope."""
    return JSONResponse(
        status_code=exc.status_code,
        content=_error_body(exc.status_code, str(exc.detail)),
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
    """Log the real error server-side, answer a generic 500 with no internals."""
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
