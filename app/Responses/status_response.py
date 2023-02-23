from pydantic import BaseModel


class StatusResponse(BaseModel):
    status: str
    version: str
    description: str
