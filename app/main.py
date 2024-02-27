from fastapi import FastAPI

from app.core.database import init_db
from app.routers import done, task

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/hello/{name}", response_model=dict)
async def say_hello(name: str) -> dict:
    return {"message": f"Hello {name}"}

app.include_router(task.router)
app.include_router(done.router)
