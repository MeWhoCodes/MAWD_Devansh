from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/{name}")
def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}"}
