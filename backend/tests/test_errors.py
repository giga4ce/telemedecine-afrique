"""Centralized error handling tests (SPEC-03)."""

from fastapi.testclient import TestClient


def test_unknown_route_returns_structured_404(client: TestClient) -> None:
    response = client.get("/does-not-exist")
    assert response.status_code == 404

    body = response.json()
    # Structured envelope, never a raw Python traceback.
    assert body == {"error": {"code": 404, "message": "Not Found"}}
    assert "Traceback" not in response.text


def test_405_is_also_enveloped(client: TestClient) -> None:
    # /health exists only for GET -> POST yields a handled 405, still structured.
    response = client.post("/health")
    assert response.status_code == 405
    assert response.json()["error"]["code"] == 405
