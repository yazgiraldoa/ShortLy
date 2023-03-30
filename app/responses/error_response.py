from pydantic import BaseModel

from app.dtos.message_dto import MessageDto


class ErrorResponse(BaseModel):
    error: MessageDto
