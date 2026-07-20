# Testing

- `pytest` + `pytest-django`, configured in `pyproject.toml`
  (`DJANGO_SETTINGS_MODULE = config.settings.local`).
- Shared factories in `tests/factories.py` — import these into
  per-app `domain/<app>/tests/` rather than redefining fixtures.
- Run: `poetry run pytest`
