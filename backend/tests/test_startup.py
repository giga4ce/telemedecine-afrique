"""Application startup tests (SPEC-03)."""

from fastapi import FastAPI

from app.main import create_app


def test_app_builds_without_error() -> None:
    app = create_app()
    assert isinstance(app, FastAPI)


def test_health_route_is_registered() -> None:
    app = create_app()
    # OpenAPI schema is the flattened public contract of mounted routers.
    assert "/health" in app.openapi()["paths"]
