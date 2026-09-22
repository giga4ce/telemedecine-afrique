"""FastAPI skeleton for the teleradiology POC (SPEC-02).

No business logic: exposes a single health endpoint used by the Docker
healthcheck and the Compose orchestration. Business routes arrive in SPEC-03.
"""

from fastapi import FastAPI

app = FastAPI(title="Telemed POC Backend", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness probe consumed by the container healthcheck."""
    return {"status": "ok"}
