FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Configure Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VENV_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/opt/poetry \
    POETRY_HOME="/opt/poetry" \
    POETRY_VENV_PATH="/opt/poetry/venv"

# Copy application code first
COPY . .

# Install dependencies
RUN poetry install

# Expose port
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "uvicorn", "claudecode.main:app", "--host", "0.0.0.0", "--port", "8000"]