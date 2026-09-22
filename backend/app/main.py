"""FastAPI application entry point (SPEC-03).

Instantiates the app, mounts routers and registers centralized error handlers.
No business model, no DICOM, no database connection (those arrive in SPEC-04+).
"""

from fastapi import FastAPI

from app.api.routes import health
from app.core.config import get_settings
from app.core.errors import register_error_handlers


def create_app() -> FastAPI:
    """Application factory: build and configure the FastAPI instance."""
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version=settings.app_version)

    register_error_handlers(app)
    app.include_router(health.router)

    return app


app = create_app()
