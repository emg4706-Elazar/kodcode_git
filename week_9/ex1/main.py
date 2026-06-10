from fastapi import FastAPI
import db
import uvicorn


app = FastAPI()


@app.post("/setup")
def post_soldiers():
    return {"status": "ok"}

@app.get("/schema")
def get_schema():
    return db.get_schema()

@app.get("/soldiers")
def get_soldiers():
    return {"soldiers": []}




