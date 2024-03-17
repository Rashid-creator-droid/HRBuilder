import uvicorn
from fastapi import FastAPI
from api.v1 import router as router_v1
from core.config import settings

app = FastAPI()

app.include_router(
    router=router_v1,
    prefix=settings.api_prefix,
)


@app.get("/")
async def HRBuild():
    return {"message": "ALLLOO TEST"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
