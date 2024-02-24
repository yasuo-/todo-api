from pydantic import BaseModel, Field, ConfigDict


class TaskBase(BaseModel):
    title: str | None = Field(None, title="Task title", description="The title of the task", examples=["sample task"])


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskBase):
    id: int
    done: bool = Field(False, title="Task done", description="The status of the task", examples=[False])

    model_config = ConfigDict(from_attributes=True)


class Task(TaskBase):
    id: int
    done: bool = Field(False, title="Task done", description="The status of the task", examples=[False])

    model_config = ConfigDict(from_attributes=True)

