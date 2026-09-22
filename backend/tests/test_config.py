"""Configuration tests (SPEC-03 + revue KAN-6 — amélioration 3)."""

import pytest

from app.core.config import Settings, get_settings


def test_settings_read_backend_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BACKEND_APP_NAME", "Custom Name")
    monkeypatch.setenv("BACKEND_APP_VERSION", "9.9.9")
    monkeypatch.setenv("BACKEND_ENVIRONMENT", "staging")

    settings = Settings()

    assert settings.app_name == "Custom Name"
    assert settings.app_version == "9.9.9"
    assert settings.environment == "staging"


def test_get_settings_returns_cached_instance() -> None:
    assert get_settings() is get_settings()


def test_get_settings_cache_isolation(monkeypatch: pytest.MonkeyPatch) -> None:
    # The autouse fixture cleared the cache; first read picks up "First".
    monkeypatch.setenv("BACKEND_APP_NAME", "First")
    first = get_settings()
    assert first.app_name == "First"

    # Clearing the cache lets a new environment take effect — proving no leak.
    get_settings.cache_clear()
    monkeypatch.setenv("BACKEND_APP_NAME", "Second")
    second = get_settings()
    assert second.app_name == "Second"
    assert first is not second
