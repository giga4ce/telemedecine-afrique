"""Health endpoint contract tests (SPEC-03).

Guards the contract already verified in KAN-5: 200 with {"status": "ok"}.
"""

from fastapi.testclient import TestClient


def test_health_returns_ok(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
