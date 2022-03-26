from fastapi import APIRouter,  Query
from fastapi.responses import Response
from enum import Enum
from typing import Optional
from ..push_engine import send_message

router = APIRouter(
    prefix='/v1'
)


class PushType(str, Enum):
    info = 'info'
    error = 'error'
    warning = 'warning'
    success = 'success'


@router.post('/ios')
async def message(
    message: str = Query(...,
                         min_length=5,
                         title='Push message',
                         description='message to be send to the device',
                         ),
    description: Optional[str] = Query('',
                                       title='Description of message',
                                       description='Description is send together with message',
                                       ),
    type: PushType = 'info'
):
    return await send_message(message, description, type)
