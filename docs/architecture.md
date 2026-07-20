# Architecture

## Layout

- `config/` — settings (split base/local/production), root urls, celery, wsgi/asgi.
- `domain/` — one folder per bounded context. `base` is cross-cutting
  (auth, dashboard, mixins, permissions). `notification` is in-app +
  email notifications, kept as its own domain from day one.
- `templates/` — mirrors `domain/` structure under `templates/domain/`,
  plus `partials/` for navbar/sidebar/footer/messages.
- `tests/factories.py` — shared factory_boy factories, imported into
  per-app `tests/` folders as those get built out.

## Conventions

1. Business logic that isn't "render a template" or "define a field"
   goes in a `services/` module inside the relevant domain app —
   not in views, not in model methods.
2. Class-based views only, split by concern
   (`views/<thing>_views.py`, not one `views.py`).
3. Models split into a package once a single file gets unwieldy,
   with `models/__init__.py` re-exporting so external imports don't
   change.
4. New feature domains get added under `domain/<feature>/` with the
   same internal shape as `notification/`: `models.py`, `admin.py`,
   `urls.py`, `services/`, `migrations/`.
5. Context processors for anything that needs to appear in every
   template (sidebar counts, badges) live in
   `domain/<app>/services/context_processors.py` and get registered
   in `config/settings/base.py`.

## Open questions

- Whether `Profile` stays a OneToOne on `User` or becomes a custom
  `AUTH_USER_MODEL`. Worth deciding before the first migration that
  touches auth, since swapping later means a data migration.
