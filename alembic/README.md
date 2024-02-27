Generic single-database configuration.

## Commands

```bash
$ docker-compose exec api alembic revision --autogenerate -m "init migration"
```

```bash
$ docker-compose exec api alembic upgrade head
```

```bash
$ docker-compose exec api alembic downgrade -1
```

```bash
$ docker-compose exec api alembic history
```

```bash
$ docker-compose exec api alembic current
```

```bash
$ docker-compose exec api alembic stamp head
```

