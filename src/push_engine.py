from .settings import engine_settings as settings
from fastapi.responses import JSONResponse
from fastapi import status
import requests

def send_message(message: str):
    
    # requests.post('https://api.mynotifier.app', {
    # "apiKey": settings.API_KEY,
    # "message": message,
    # "description": "This is cool",
    # "type": "info", # info, error, warning or success
    # })
    
    return (f"Message {settings.API_KEY} send OK",status.HTTP_200_OK)