import pytest
from pydantic_core import MultiHostUrl

from app.core.config import Settings, get_settings


@pytest.fixture(autouse=True)
def setup_env(mocker):  # noqa: ANN001, PT004
    mocker.patch.dict(
        "os.environ",
        {
            "POSTGRES_SERVER": "test-server",
            "POSTGRES_USER": "user",
            "POSTGRES_PASSWORD": "password",
            "POSTGRES_DB": "testdb",
            "POSTGRES_PORT": "5432",
        },
    )


PASSWORD = "password"  # noqa: S105
DATABASE_URI = MultiHostUrl("postgresql+psycopg2://user:password@test-server:5432/testdb")


class TestConfig:
    def test_settings_load_from_env(self):
        settings = get_settings()

        assert settings.POSTGRES_SERVER == "test-server"
        assert settings.POSTGRES_USER == "user"
        assert settings.POSTGRES_PASSWORD == PASSWORD
        assert settings.POSTGRES_DB == "testdb"
        assert settings.POSTGRES_PORT == "5432"
        assert settings.SQLALCHEMY_DATABASE_URI == DATABASE_URI

    def test_assemble_db_connection_with_explicit_uri(self):
        uri = "postgresql+psycopg2://user:password@localhost:54320/testdb"
        settings = Settings(SQLALCHEMY_DATABASE_URI=uri)
        assert settings.SQLALCHEMY_DATABASE_URI == DATABASE_URI

    def test_get_settings(self):
        settings = get_settings()
        assert settings.POSTGRES_SERVER == "test-server"
        assert settings.POSTGRES_USER == "user"
        assert settings.POSTGRES_PASSWORD == PASSWORD
        assert settings.POSTGRES_DB == "testdb"
        assert settings.POSTGRES_PORT == "5432"
        assert settings.SQLALCHEMY_DATABASE_URI == DATABASE_URI
