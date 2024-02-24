from fastapi import APIRouter

router = APIRouter()


@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done(task_id: int) -> None:  # noqa: ARG001
    return None


@router.delete("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_not_done(task_id: int) -> None:  # noqa: ARG001
    return None
