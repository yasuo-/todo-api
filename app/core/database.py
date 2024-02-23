from collections.abc import Generator

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlmodel import Session, create_engine

from app.core.config import settings


class DatabaseURINotSetError(ValueError):
    """Exception raised when the SQLALCHEMY_DATABASE_URI is not set."""
    def __init__(self, message: str = "SQLALCHEMY_DATABASE_URI is not set") -> None:
        self.message = message
        super().__init__(self.message)


if settings.SQLALCHEMY_DATABASE_URI is None:
    raise DatabaseURINotSetError
else:
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, echo=False, future=True)
    session_factory = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True))


def get_session() -> Generator[Session, None, None]:
    """Get a session from the database."""
    db = None
    try:
        db = session_factory()
        yield db
        db.commit()
    except Exception: # noqa: BLE001
        if db:
            db.rollback()
    finally:
        if db:
            db.close()
