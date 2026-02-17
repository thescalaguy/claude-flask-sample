FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry-core

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir .

COPY . .
RUN pip install --no-cache-dir .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app()"]
