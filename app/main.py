from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
import uvicorn

from starlette.exceptions import HTTPException as StarletteHTTPException
from app.constants.general_constants import HTTP_STATUS
from app.responses.error_response import ErrorResponse
from configurations.settings import settings
from app.dtos.message_dto import MessageDto
from controllers import router

app = FastAPI()
app.include_router(router=router, prefix=settings.base_path)


@app.on_event("startup")
async def startup_event():
    from alembic.config import Config
    from alembic import command

    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    msg = MessageDto(
        message=HTTP_STATUS.get(str(exc.status_code)),
        details=exc.detail
    )
    content = ErrorResponse(error=msg)
    return JSONResponse(content=content.dict(), status_code=exc.status_code)


@app.exception_handler(Exception)
async def generic_error_handler(request, exc):
    msg = MessageDto(message="Internal server error", details="Oops, please try again later")
    content = ErrorResponse(error=msg)
    return JSONResponse(content=content.dict(), status_code=500)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True, loop='asyncio')
