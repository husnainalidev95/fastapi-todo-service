from sqlmodel import Session
from app.models import Task, Board
from app.modules.tasks.schemas import TaskCreate

# Takes the whole Board, not just an id, so the caller has to have loaded it -
# which means it has already checked the board exists.
def create_task(session: Session, board: Board, data: TaskCreate) -> Task:
    # board_id comes from the URL, not the body, so it's merged in here. It has to
    # go in during validation - Task requires it and would reject the data without.
    task = Task.model_validate(data, update={"board_id": board.id})
    session.add(task)
    session.commit()
    session.refresh(task)
    return task