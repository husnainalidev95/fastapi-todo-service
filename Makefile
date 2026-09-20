# Shortcuts for Alembic. Everything runs through "docker compose exec api"
# because the DATABASE_URL and the "db" hostname only exist inside the container.

# Tells Make these are commands, not files to build - without it, Make would
# skip "migrate" if a file named "migrate" ever existed in this folder.
.PHONY: revision migrate

# Generate a new migration by diffing your models against the live database.
# Usage: make revision m="create board and task tables"
# Always read the generated file before applying it.
revision:
	docker compose exec api uv run alembic revision --autogenerate -m "$(m)"

# Apply every migration that hasn't run yet.
migrate:
	docker compose exec api uv run alembic upgrade head
