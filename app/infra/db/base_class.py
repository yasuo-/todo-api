import datetime
from uuid import UUID, uuid4

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID as pgUUID  # noqa: N811
from sqlmodel import Field, SQLModel, text


class BaseModel(SQLModel):
    id: UUID = Field(default_factory=uuid4, sa_column=Column(pgUUID(as_uuid=True), primary_key=True))
    created_at: datetime = Field(
        nullable=False,
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")},
        title="Date Created",
    )
    updated_at: datetime = Field(
        nullable=False,
        sa_column_kwargs={
            "server_default": text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        },
        title="Date Updated",
    )
