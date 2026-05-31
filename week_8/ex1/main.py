import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/ping")
def ping():
    return {"status": "pong"}

@app.get("/greet/{name}")
def greet(name):
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",port=8000)