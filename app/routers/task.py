from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
async def list_tasks():
    pass


@router.post("/tasks")
async def create_task():
    pass


@router.get("/tasks/{task_id}")
async def get_task(task_id: int):
    pass


@router.put("/tasks/{task_id}")
async def update_task(task_id: int):
    pass


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    pass
