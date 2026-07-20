# BOQ App

## Setup

```bash
poetry install
cp .env.example .env      # then fill in SECRET_KEY etc.
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
poetry run python manage.py runserver
```

## Structure

See `docs/architecture.md` for the domain layout and conventions.
