from fastapi import APIRouter

import app.schemas.task as tasks_schema

router = APIRouter()


@router.get("/tasks", response_model=list[tasks_schema.Task])
async def list_tasks() -> list[tasks_schema.Task]:
    return [
        tasks_schema.Task(id=1, title="Task 1", done=False),
        tasks_schema.Task(id=2, title="Task 2", done=True),
    ]


@router.post("/tasks", response_model=tasks_schema.TaskCreateResponse)
async def create_task(body: tasks_schema.TaskCreate) -> tasks_schema.TaskCreateResponse:
    return tasks_schema.TaskCreateResponse(id=1, title=body.title, done=False)


@router.get("/tasks/{task_id}", response_model=tasks_schema.Task)
async def get_task(task_id: int) -> tasks_schema.Task:
    return tasks_schema.Task(id=task_id, title="Task 1", done=False)


@router.put("/tasks/{task_id}", response_model=tasks_schema.TaskCreateResponse)
async def update_task(task_id: int, body: tasks_schema.TaskCreate) -> tasks_schema.TaskCreateResponse:
    return tasks_schema.TaskCreateResponse(id=task_id, title=body.title, done=False)


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int) -> None:  # noqa: ARG001
    return None
