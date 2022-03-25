import os
from typing import Optional

import pydantic

ENV_FILE = os.getenv("ENV_FILE", ".env")


class BaseSettings(pydantic.BaseSettings):
    """Base class for loading settings.
    The setting variables are loaded from environment settings first, then from the defined env_file.

    Different groups/contexts of settings are created using different classes, that can define an env_prefix which
    will be concatenated to the start of the variable name."""
    class Config:
        env_file = ENV_FILE

# Push engine config


class PushEngineSettings(BaseSettings):
    ''' push engine settings'''
    # API key see
    # https://medium.com/mynotifier/python-sending-push-notifications-to-your-phone-feaeedcbaac1
    API_KEY: str
    # myNotifier URL
    URL = "https://api.mynotifier.app"

    class Config(BaseSettings.Config):
        env_prefix = "PUSH_ENGINE_"


class APISettings(BaseSettings):
    """Settings related with the FastAPI server"""
    host: str = "localhost"
    port: int = 5000

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class RequestLoggingSettings(BaseSettings):
    """Settings related with the logging of requests"""
    level: str = "DEBUG"
    serialize: bool = False

    class Config(BaseSettings.Config):
        env_prefix = "REQUEST_LOG_"


api_settings = APISettings()
request_logging_settings = RequestLoggingSettings()
engine_settings = PushEngineSettings()
