import os 
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine

# Built once, when this module is first imported, and reused for the life of the
# process. The engine owns a pool of open connections to Postgres - building one
# per request would mean a fresh TCP connection and handshake on every call.
# Reading the environment here also means a missing DATABASE_URL crashes the app
# at startup rather than on the first request that happens to need the database.
engine = create_engine(os.environ["DATABASE_URL"])

# One session per request, never shared. A session holds the objects you've
# loaded and tracks what you changed, so two requests sharing one would see each
# other's half-finished work.
def get_session():
    # "with" closes the session on the way out even if the endpoint raises,
    # which is what stops connections leaking back out of the pool.
    with Session(engine) as session:
        # FastAPI runs the endpoint right here, at the yield, and comes back to
        # finish this function once the response is done.
        yield session

# Just a named type, so endpoints can say "session: SessionDep" instead of
# repeating "session: Session = Depends(get_session)" on every route.
SessionDep = Annotated[Session, Depends(get_session)]
