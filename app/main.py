from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", response_model=dict)
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
