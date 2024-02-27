from sqlmodel import Field

from app.infra.db.base_class import BaseModel


class User(BaseModel, table=True):
    __tablename__ = "users"
    name: str = Field(max_length=50)
