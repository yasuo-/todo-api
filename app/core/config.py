import logging
from functools import lru_cache

from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """Settings for the application.
    This class is used to read the environment variables from the .env file.
    """
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="after")
    def assemble_db_connection(cls, v: str | None, values: ValidationInfo) -> PostgresDsn | None:  # noqa: N805
        if isinstance(v, str):
            return v

        port = values.data.get("POSTGRES_PORT")

        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            host=values.data.get("POSTGRES_SERVER"),
            port=int(port) if port else 5432,
            path=values.data.get("POSTGRES_DB") or "",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
        )


@lru_cache
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()
