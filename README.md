# claudecode

A Python project with FastAPI and PostgreSQL.

## Setup

### With Docker
```bash
docker-compose up --build
```

### Local Development
```bash
poetry install
poetry run uvicorn claudecode.main:app --reload
```

## Database

PostgreSQL with Alembic migrations.

```bash
poetry run alembic revision -m "description" --autogenerate
poetry run alembic upgrade head
```

## Project Structure

- `claudecode/` - Main package directory
- `alembic/` - Database migrations
- `tests/` - Test directory
- `pyproject.toml` - Poetry configuration