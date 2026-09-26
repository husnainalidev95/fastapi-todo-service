from fastapi import APIRouter, HTTPException

from app.db import SessionDep
from app.modules.boards.schemas import BoardCreate, BoardPublic, BoardUpdate
from app.modules.boards.service import create_board, list_boards, get_board, update_board, delete_board

# Like @Controller('boards') - every route below starts with /boards.
# tags groups these routes under one heading in /docs.
router = APIRouter(prefix="/boards", tags=["boards"])

# response_model strips the returned Board down to BoardPublic's fields, so a
# column added to the table later can't leak out by accident.
# 201 instead of the default 200, because something new was created.
@router.post("/", response_model=BoardPublic, status_code=201)
# Plain def, not async: the session is synchronous and would block the event
# loop. FastAPI runs plain def routes in a thread pool instead.
# FastAPI reads "data" from the JSON body and builds "session" by calling
# get_session() - neither is created by us.
def create(data: BoardCreate, session: SessionDep):
    return create_board(session, data)

# list[...] because this returns every board, not one. Each item is filtered
# through BoardPublic the same way as a single board.
@router.get("/", response_model=list[BoardPublic])
def list_all(session: SessionDep):
    return list_boards(session)

# {board_id} is a path parameter. FastAPI matches it to the argument of the same
# name and turns "abc" into a 422, because the argument is typed as int.
@router.get("/{board_id}", response_model=BoardPublic)
def get_one(board_id: int, session: SessionDep):
    board = get_board(session, board_id)
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return board

@router.patch("/{board_id}", response_model=BoardPublic)
def update_one(board_id: int, data: BoardUpdate, session: SessionDep):
    board = get_board(session, board_id)
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return update_board(session, board, data)

# 204 means success with no body - there's nothing left to send back, so no
# response_model either.
@router.delete("/{board_id}", status_code=204)
def delete_one(board_id: int, session: SessionDep):
    board = get_board(session, board_id)
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return delete_board(session, board)