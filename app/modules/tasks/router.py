from fastapi import APIRouter, HTTPException

from app.db import SessionDep
from app.modules.tasks.schemas import TaskPublic, TaskCreate
from app.modules.tasks.service import create_task
from app.modules.boards.service import get_board

# No prefix, because routes here start with either /boards/... or /tasks/...
# (shallow nesting), so each route spells out its full path.
router = APIRouter(tags=["tasks"])

# Nested under the board because a task can't exist without one.
@router.post("/boards/{board_id}/tasks", response_model=TaskPublic, status_code=201)
def create_one(board_id: int, data: TaskCreate, session: SessionDep):
    # Check first so a bad board_id is a clear 404. Otherwise Postgres rejects
    # the insert on the foreign key and the client only sees a 500.
    board = get_board(session, board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return create_task(session, board, data)