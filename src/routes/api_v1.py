from fastapi import APIRouter
from fastapi.responses import Response
from enum import EnumImmutableError

import requests
from ..push_engine import send_message

router = APIRouter(
    prefix = '/v1'
)


class PushType(str, Enum):
    info = 'info'
    error = 'error'
    warning = 'warning'
    success = 'success'    

@router.post('/ios/{message}')
def message(message: str, response: Response):
    _response_message, _status_code = send_message(message)
    response.status_code = _status_code
    return {"message" : _response_message}