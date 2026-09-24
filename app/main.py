from fastapi import FastAPI
from app.modules.boards.router import router as boards_router

app = FastAPI()

app.include_router(boards_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
