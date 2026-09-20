from sqlmodel import SQLModel, Field


# table=True is what makes this a real database table, named "board"
# (SQLModel lowercases the class name). Without it this would just be
# a plain Pydantic model used for validation and nothing else.
class Board(SQLModel, table=True):
    # Primary key - Postgres generates the value, so it's empty until saved
    id: int | None = Field(default=None, primary_key=True)
    # No default means the column is NOT NULL and must always be provided
    name: str
    # default="" gives a NOT NULL column that starts empty, rather than nullable
    description: str = Field(default="")
