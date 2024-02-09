from fastapi import FastAPI

from app.routers import task, done

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.get("/hello/{name}", response_model=dict)
async def say_hello(name: str) -> dict:
    return {"message": f"Hello {name}"}

app.include_router(task.router)
app.include_router(done.router)
