from sqlmodel import SQLModel

# No table=True, so this is only a Pydantic model for validating JSON, never a
# database table. Holds the fields every board schema shares.
class BoardBase(SQLModel):
    # No default means required - FastAPI answers 422 before our code even runs
    name: str
    description: str = ""

# What the client sends. No id, so clients can't pick their own primary key.
class BoardCreate(BoardBase):
    pass

# What the API returns. id is a plain int, not optional, because a board we
# send back has already been saved and Postgres has given it one.
class BoardPublic(BoardBase):
    id: int
