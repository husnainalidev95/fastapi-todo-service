# Linux + Python 3.14, stripped-down base image
FROM python:3.14-slim

# Grab the uv binary out of uv's official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Working directory inside the container
WORKDIR /app

# Deps only - these rarely change
COPY pyproject.toml uv.lock ./

# Install exact versions from uv.lock - this layer gets cached
RUN uv sync --locked

# Your code - changes constantly, so it goes last
COPY . .

# Runs at container start, not at build time
CMD ["uv", "run", "fastapi", "dev", "--host", "0.0.0.0"]
