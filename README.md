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

## Testing

Run tests using pytest:

```bash
# Run all tests
poetry run pytest

# Run tests with verbose output
poetry run pytest -v

# Run tests in a specific directory
poetry run pytest tests/

# Run tests with coverage
poetry run pytest --cov=claudecode
```

## Custom Commands

This project includes custom Claude Code commands for issue management:

### /issue-create
Creates GitHub issues using natural language input. The command translates user requests into proper `gh issue create` commands with appropriate labels, assignees, milestones, and projects.

**Usage**: `/issue-create <description>`

**Example**: 
```
/issue-create The login page throws HTTP 500 on desktop Chrome. Assign to bob, label as bug and backend.
```

### /issue-fix
Automated development workflow for fixing GitHub issues. Follows a structured approach: investigate → implement → deliver.

**Usage**: `/issue-fix <issue_number>`

**Workflow**:
1. **Investigate**: Views issue details and summarizes the problem
2. **Implement**: Creates/switches to branch, writes tests first (TDD), makes minimal code changes
3. **Deliver**: Runs full test suite, creates PR, requests review

**Example**:
```
/issue-fix 17
```

## Project Structure

- `claudecode/` - Main package directory
- `alembic/` - Database migrations
- `tests/` - Test directory
- `.claude/commands/` - Custom Claude Code commands
- `pyproject.toml` - Poetry configuration