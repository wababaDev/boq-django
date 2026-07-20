from .base import *  # noqa: F401,F403

DEBUG = True
ALLOWED_HOSTS = ["*"]

# SQLite by default for local dev — override via .env if you want to
# point at a real Postgres/MSSQL instance while developing.

INSTALLED_APPS += [  # noqa: F405
    # "debug_toolbar",
]
