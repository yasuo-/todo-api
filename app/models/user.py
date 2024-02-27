from uuid import uuid4, UUID

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlmodel import Field

from app.infra.db.base_class import BaseModel


class User(BaseModel, table=True):
    __tablename__ = "users"
    id: UUID = Field(default_factory=uuid4, sa_column=Column(pgUUID(as_uuid=True), primary_key=True))
    name: str = Field(max_length=50)
