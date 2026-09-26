from sqlmodel import SQLModel
from app.models.task import Status

class TaskBase(SQLModel):
    title: str
    description: str = ""
    status: Status = Status.triage

class TaskCreate(TaskBase):
    pass

class TaskPublic(TaskBase):
    id: int
    board_id: int

class TaskUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
    status: Status | None = None
    board_id: int | None = None