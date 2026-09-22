"""Centralized error handling tests (SPEC-03 + revue KAN-6).

Guarantees the non-leak contract: no HTTPException detail, no raw validation
input, no stack trace / internal path ever reaches the client.
"""

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel

from app.core.errors import PublicHTTPException
from app.main import create_app


class _Payload(BaseModel):
    value: int


@pytest.fixture
def error_client() -> TestClient:
    """App augmented with test-only routes that exercise each error path."""
    app = create_app()

    @app.post("/_test/echo")
    def _echo(payload: _Payload) -> dict[str, int]:
        return {"value": payload.value}

    @app.get("/_test/boom")
    def _boom() -> None:
        raise RuntimeError("boom-secret /srv/secret/password")

    @app.get("/_test/http-detail")
    def _http_detail() -> None:
        raise HTTPException(status_code=400, detail="internal-path-/srv/secret")

    @app.get("/_test/public")
    def _public() -> None:
        raise PublicHTTPException(
            status_code=403,
            public_message="Accès non autorisé",
            detail="internal-reason /srv/secret",
        )

    # raise_server_exceptions=False → the 500 handler response is returned
    # instead of the exception being re-raised into the test.
    return TestClient(app, raise_server_exceptions=False)


# --- Existing contract (unchanged) -----------------------------------------


def test_unknown_route_returns_structured_404(client: TestClient) -> None:
    response = client.get("/does-not-exist")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": 404, "message": "Not Found"}}
    assert "Traceback" not in response.text


def test_405_is_also_enveloped(client: TestClient) -> None:
    response = client.post("/health")
    assert response.status_code == 405
    assert response.json()["error"]["code"] == 405


# --- Bloquant 2 : garanties 422 / 500 / HTTPException -----------------------


def test_422_does_not_echo_input(error_client: TestClient) -> None:
    response = error_client.post("/_test/echo", json={"value": "notanumber"})
    assert response.status_code == 422
    # The submitted value must never be reflected back.
    assert "notanumber" not in response.text
    body = response.json()
    assert body["error"]["code"] == 422
    for field in body["error"]["fields"]:
        assert set(field) == {"loc", "msg", "type"}


def test_500_hides_all_internals(error_client: TestClient) -> None:
    response = error_client.get("/_test/boom")
    assert response.status_code == 500
    assert response.json() == {
        "error": {"code": 500, "message": "Internal Server Error"}
    }
    for leak in ("boom-secret", "/srv/secret", "Traceback", "RuntimeError"):
        assert leak not in response.text


def test_http_exception_detail_is_not_leaked(error_client: TestClient) -> None:
    # This is the test that would have caught bloquant 1.
    response = error_client.get("/_test/http-detail")
    assert response.status_code == 400
    assert "internal-path-/srv/secret" not in response.text
    assert response.json() == {"error": {"code": 400, "message": "Bad Request"}}


def test_public_http_exception_exposes_only_public_message(
    error_client: TestClient,
) -> None:
    response = error_client.get("/_test/public")
    assert response.status_code == 403
    body = response.json()
    assert body["error"]["message"] == "Accès non autorisé"
    assert "internal-reason" not in response.text
    assert "/srv/secret" not in response.text
