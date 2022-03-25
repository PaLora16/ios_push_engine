from fastapi import FastAPI

from .routes import api_v1


def setup_routes(app: FastAPI):
    """Each Router specified in routes/* must be referenced in setup_routes(),
    as a new app.include_router() call."""
    app.include_router(
        api_v1.router,
        tags=["iOS push notification service"]
    )


TAGS_METADATA = [
    {
        "name": "api",
        "description": "sends message to registered iOS device."
    }
]
