from datetime import datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as pgUUID  # noqa: N811
from sqlmodel import DateTime, Field, Relationship

from app.infra.db.base_class import BaseModel

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Task(BaseModel, table=True):
    __tablename__ = "tasks"
    id: UUID = Field(default_factory=uuid4, sa_column=Column(pgUUID(as_uuid=True), primary_key=True))
    title: str = Field(max_length=255)
    description: str = Field(max_length=1000)

    creator_id: str = Field(sa_column=Column(pgUUID(as_uuid=True), ForeignKey("users.id")))
    done: Optional["TaskDone"] = Relationship(back_populates="task")


class TaskDone(BaseModel, table=True):
    __tablename__ = "task_dones"
    id: UUID = Field(default_factory=uuid4, sa_column=Column(pgUUID(as_uuid=True), primary_key=True))
    done_at: datetime = Field(sa_column=Column(DateTime, default=datetime.utcnow))
    task: Optional["Task"] = Relationship(back_populates="done")
