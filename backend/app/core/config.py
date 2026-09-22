"""Typed application configuration (SPEC-03).

Settings are read from environment variables via pydantic-settings, keeping
configuration externalized as in poc/.env.example. No secret is hardcoded and
no database configuration is introduced here (that arrives in SPEC-04).
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings, overridable through `BACKEND_*` env variables."""

    app_name: str = "Telemed POC Backend"
    app_version: str = "0.1.0"
    environment: str = "local"

    model_config = SettingsConfigDict(
        env_prefix="BACKEND_",
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance (single read of the environment)."""
    return Settings()
