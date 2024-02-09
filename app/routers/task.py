from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
async def list_tasks() -> dict:
    pass


@router.post("/tasks")
async def create_task() -> dict:
    pass


@router.get("/tasks/{task_id}")
async def get_task(task_id: int) -> dict:
    pass


@router.put("/tasks/{task_id}")
async def update_task(task_id: int) -> dict:
    pass


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int) -> dict:
    pass
