from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()


@router.get('/')
def check(response: Response):
    response.status_code = 200
    return {"Push notification Api status": "OK"}
