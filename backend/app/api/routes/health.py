"""Health route (SPEC-03).

Same observable contract as delivered in KAN-5: GET /health -> 200 {"status": "ok"}.
Moved under a dedicated router; no behavior change.
"""

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    """Liveness probe consumed by the container healthcheck."""
    return {"status": "ok"}
