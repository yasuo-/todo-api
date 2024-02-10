from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, title="Task title", description="The title of the task", example="sample task")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskBase):
    id: int
    done: bool = Field(False, title="Task done", description="The status of the task", example=False)

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, title="Task done", description="The status of the task", example=False)

    class Config:
        orm_mode = True

