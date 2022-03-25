import uvicorn
from fastapi import FastAPI

from .middlewares import request_handler
from .routers import setup_routes
# from .routers import TAGS_METADATA
from .settings import api_settings

app = FastAPI(
    # openapi_tags=TAGS_METADATA
)
app.middleware("http")(request_handler)
setup_routes(app)


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app,
        host=api_settings.host,
        port=api_settings.port
    )
