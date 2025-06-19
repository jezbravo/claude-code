# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project named "claudecode" managed with Poetry. The project is in its initial setup phase with a basic package structure.

## Development Commands

### Package Management
- `poetry install` - Install dependencies
- `poetry add <package>` - Add a new dependency
- `poetry add --group dev <package>` - Add a development dependency

### Testing
- `poetry run pytest` - Run tests (once pytest is added as dependency)
- `poetry run pytest tests/` - Run all tests in tests directory
- `poetry run pytest -v` - Run tests with verbose output

### Build and Distribution
- `poetry build` - Build the package
- `poetry publish` - Publish to PyPI (when ready)

## Project Structure

- `claudecode/` - Main package directory containing the core module
- `tests/` - Test directory following pytest conventions
- `pyproject.toml` - Poetry configuration and project metadata

## Architecture Notes

The project follows a standard Python package layout with Poetry for dependency management. The main package code resides in the `claudecode/` directory, with tests in a separate `tests/` directory at the project root.