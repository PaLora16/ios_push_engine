from fastapi import FastAPI

from .routes import api_v1, hcheck


def setup_routes(app: FastAPI):
    """Each Router specified in routes/* must be referenced in setup_routes(),
    as a new app.include_router() call."""
    app.include_router(
        api_v1.router,
        tags=["ios push notification service"]
    )
    app.include_router(
        hcheck.router,
        tags=["healthcheck endpoint"]
    )
