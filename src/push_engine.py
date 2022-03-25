from .settings import engine_settings as settings
from fastapi.responses import JSONResponse
from fastapi import status
import requests

async def send_message(message: str, description: str, type: str):
    
    requests.post(settings.URL, 
    {
    "apiKey": settings.API_KEY,
    "message": message,
    "description": description,
    "type": type, 
    })
    
    respose : str = ','.join([message,description,type])
    
    return (f"Message {respose } send OK",status.HTTP_200_OK)