from datetime import datetime

from sqlmodel import Field, SQLModel, text


class BaseModel(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")},
        title="Date Created",
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP"), "onupdate": datetime.now},
        title="Date Updated",
    )
