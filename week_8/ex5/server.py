from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/greet")
def greet(name="world"):
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000)

