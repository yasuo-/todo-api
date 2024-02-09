from fastapi import APIRouter

router = APIRouter()


@router.put("/tasks/{task_id}/done")
async def mark_task_as_done(task_id: int) -> dict:
    pass


@router.delete("/tasks/{task_id}/done")
async def mark_task_as_not_done(task_id: int) -> dict:
    pass
