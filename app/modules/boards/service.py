from sqlmodel import Session, select
from app.models import Board
from app.modules.boards.schemas import BoardCreate

# The session is passed in rather than created here, so the router controls its
# lifetime and tests can hand in one pointed at a test database.
def create_board(session: Session, data: BoardCreate) -> Board:
    # Copies the request fields onto a real table object. id is still None.
    board = Board.model_validate(data)
    # Only queues it - nothing reaches Postgres until commit
    session.add(board)
    # Runs the INSERT. Without this the board vanishes when the session closes.
    session.commit()
    # Reloads the row so board.id holds the value Postgres just generated
    session.refresh(board)
    return board

# Read-only, so there's nothing to commit - just a SELECT of every row
def list_boards(session: Session) -> list[Board]:
    return session.exec(select(Board)).all()