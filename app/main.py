from fastapi import FastAPI
import uvicorn

from controllers import router

app = FastAPI()
app.include_router(router=router, prefix='/shortly/api')


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True, loop='asyncio')
