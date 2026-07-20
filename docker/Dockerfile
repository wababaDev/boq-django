FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root --only main

COPY . /app

RUN python manage.py collectstatic --noinput --settings=config.settings.production || true

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
