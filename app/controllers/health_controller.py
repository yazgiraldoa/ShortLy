from fastapi import APIRouter

from app.responses.status_response import StatusResponse
from app.configurations.settings import settings

api = APIRouter()


@api.get('/health')
def health_check() -> StatusResponse:
    return StatusResponse(
        status="up",
        version=settings.commit,
        description=settings.description
    )
