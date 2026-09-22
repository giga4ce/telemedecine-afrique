"""Shared pytest fixtures (SPEC-03)."""

import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture
def client() -> TestClient:
    """A TestClient bound to a freshly built application."""
    return TestClient(create_app())
