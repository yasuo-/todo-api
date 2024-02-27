from datetime import datetime

from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False, title="Date Created")
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False, title="Date Updated")
