from fastapi import APIRouter

from app.controllers import health_controller

router = APIRouter()

router.include_router(health_controller.api)
