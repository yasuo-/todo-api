# Todo API


## Install

```bash
$ docker-compose up -d --build
```

## Packages

FastAPI - https://fastapi.tiangolo.com/
SQLAlchemy - https://www.sqlalchemy.org/
SQLModel - https://sqlmodel.tiangolo.com/
Alembic - https://alembic.sqlalchemy.org/en/latest/
Pydantic - https://pydantic-docs.helpmanual.io/
Ruff - https://ruff.readthedocs.io/en/latest/

## Test

```bash
$ docker-compose exec api pytest
```

```bash
$ docker-compose exec api pytest --cov
```

```bash
$ docker-compose exec api pytest --cov --cov-report=html
```

## Ruff

```bash
$ docker-compose exec api ruff check .
```

```bash
$ docker-compose exec api ruff check . --fix
```
