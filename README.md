# claude-flask-sample

A REST API for math operations built with Flask, Peewee, and Postgres.

## Prerequisites

- Python 3.13+
- Docker and Docker Compose

## Setup

Start Postgres:

```bash
docker compose up -d
```

Install dependencies:

```bash
pip install .
```

Run database migrations:

```bash
yoyo apply --database postgresql://postgres:postgres@localhost:5432/postgres ./migrations
```

## Running

```bash
gunicorn --bind 0.0.0.0:8000 "app:create_app()"
```

## API

### POST /add

```bash
curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"a": 2, "b": 3}'
```

```json
{"result": 5}
```

### POST /divide

```bash
curl -X POST http://localhost:8000/divide -H "Content-Type: application/json" -d '{"a": 10, "b": 2}'
```

```json
{"result": 5.0}
```

## Testing

```bash
python -m pytest tests/ -v
```

Requires Postgres to be running.

## Docker

```bash
docker build -t claude-flask-sample .
```
