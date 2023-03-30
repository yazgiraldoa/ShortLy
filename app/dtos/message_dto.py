from pydantic import BaseModel


class MessageDto(BaseModel):
    message: str
    details: str
