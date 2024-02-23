from functools import lru_cache

from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings


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

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    def assemble_db_connection(cls, v: str | None, values: ValidationInfo) -> PostgresDsn | None:  # noqa: N805
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+psycopg",
            user=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_SERVER"),
            port=int(values.data.get("POSTGRES_PORT")),
            path=f"/{values.data.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
