"""Shared pytest fixtures (SPEC-03).

Note (revue KAN-6 — amélioration 2) : TestClient s'appuie sur httpx 0.28. Starlette
émet une StarletteDeprecationWarning recommandant `httpx2` ; migration différée et
tracée dans pyproject.toml (`filterwarnings`) — httpx2 est trop récent pour le POC.
"""

import pytest
from fastapi.testclient import TestClient

from app.core.config import get_settings
from app.main import create_app


@pytest.fixture(autouse=True)
def _clear_settings_cache() -> None:
    """Isolate the module-level `get_settings` lru_cache between tests.

    Without this, a test that sets BACKEND_* env vars could leak its cached
    Settings into a later test. Cleared before and after every test.
    """
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


@pytest.fixture
def client() -> TestClient:
    """A TestClient bound to a freshly built application."""
    return TestClient(create_app())
