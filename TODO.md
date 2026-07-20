# TODO

- [ ] `poetry install` and confirm the project boots
- [ ] Decide on custom `AUTH_USER_MODEL` vs `Profile` OneToOne (currently OneToOne — swap early if going custom, it's painful later)
- [ ] Wire Postgres for production settings
- [ ] Build first real feature domain (e.g. `domain/loan/`)
- [ ] Signal to auto-create `Profile` on user creation (`domain/base/signals.py` + `apps.py` ready())
- [ ] Docker compose for local Postgres + Redis
- [ ] CI: ruff + black + pytest
