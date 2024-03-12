import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def HRBuild():
    return {"message": "ALLLOO"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
