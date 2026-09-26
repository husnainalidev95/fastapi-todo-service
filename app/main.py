from fastapi import FastAPI
from app.modules.boards.router import router as boards_router
from app.modules.tasks.router import router as tasks_router

app = FastAPI()

app.include_router(boards_router)
app.include_router(tasks_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
