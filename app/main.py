from fastapi import FastAPI
import uvicorn

from configurations.settings import settings
from controllers import router

app = FastAPI()
app.include_router(router=router, prefix=settings.base_path)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True, loop='asyncio')
