from .settings import engine_settings as settings
from fastapi import status, HTTPException
import requests


async def send_message(message: str, description: str, type: str):
    '''Send push message request to myNotifier host URL'''
    if not settings.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="API KEY not found")
    response = requests.post(settings.URL,
                             {
                                 "apiKey": settings.API_KEY,
                                 "message": message,
                                 "description": description,
                                 "type": type
                             })
    return response.json()
