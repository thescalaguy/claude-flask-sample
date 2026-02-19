# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- **Start Postgres:** `docker compose up -d`
- **Run all tests:** `python -m pytest tests/ -v` (requires Postgres running)
- **Run a single test:** `python -m pytest tests/test_add.py::test_add_integers -v`
- **Run tests for one file:** `python -m pytest tests/test_add.py -v`
- **Formatting:** `black .` (also enforced via pre-commit hook)
- **Run app locally:** `gunicorn --bind 0.0.0.0:8000 "app:create_app()"`
- **Build Docker image:** `docker build -t claude-flask-sample .`

## Architecture

Flask REST API for math operations with Postgres persistence, managed with Poetry.

- **`app/__init__.py`** — App factory (`create_app()`) that registers blueprints
- **`app/routes.py`** — `math_bp` blueprint with POST endpoints (`/add`, `/divide`). Each endpoint validates input, persists operands to the database, and returns the result.
- **`app/models.py`** — Peewee ORM models (`Addition`, `Quotient`) using `PooledPostgresqlDatabase` for thread-safe connection pooling with Gunicorn
- **`migrations/`** — yoyo-migrations SQL files for schema changes (each migration has a `.sql` and `.rollback.sql`)

## Testing

Tests require a running Postgres instance (`docker compose up -d`). The `client` fixture in `tests/conftest.py` creates and drops tables per test invocation. Test files import models directly to verify database persistence.

## Conventions

- Formatter: Black (via pre-commit hooks)
- Each math operation gets its own Peewee model and test file
- Routes return JSON with `{"result": ...}` on success or `{"error": ...}` with 400 status on failure
