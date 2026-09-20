# Importing the models here is what registers their tables on SQLModel.metadata.
# That metadata is what Alembic reads when autogenerating migrations, so every
# new model file needs a line added below or its table will be invisible.
from app.models.board import Board
from app.models.task import Task, Status

# Lets other modules write "from app.models import Board, Task"
__all__ = ["Board", "Task", "Status"]
