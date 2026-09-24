from fastapi import APIRouter

from app.db import SessionDep
from app.modules.boards.schemas import BoardCreate, BoardPublic
from app.modules.boards.service import create_board, list_boards

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