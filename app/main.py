from fastapi import FastAPI
import uvicorn

from configurations.settings import settings
from controllers import router

app = FastAPI()
app.include_router(router=router, prefix=settings.base_path)


@app.on_event("startup")
async def startup_event():
    from alembic.config import Config
    from alembic import command

    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True, loop='asyncio')
