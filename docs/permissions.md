# Permissions

Role-based access lives in two places:

- `domain/base/mixins.py` — class-based view mixins
  (`RoleRequiredMixin`, subclass with `allowed_roles = [...]`).
- `domain/base/permissions.py` — plain functions for use inside
  services where a mixin doesn't fit.

`Profile.role` (see `domain/base/models.py`) drives both.
