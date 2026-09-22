# FastAPI skeleton image — installed with uv, served by Uvicorn on 8000.
# uv pinned to the host toolchain version for reproducible local<->OVH builds.
FROM python:3.12-slim

# uv binary copied from its official pinned image (no curl|sh installer).
COPY --from=ghcr.io/astral-sh/uv:0.11.9 /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Dependency layer: cached until the lockfile changes.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

# Application layer.
COPY app ./app
RUN uv sync --frozen --no-dev

EXPOSE 8000

# Container healthcheck hits /health (no curl in slim image → urllib).
HEALTHCHECK --interval=10s --timeout=3s --start-period=15s --retries=5 \
    CMD ["python", "-c", "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8000/health').status==200 else 1)"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
