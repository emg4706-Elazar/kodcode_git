from fastapi import FastAPI
import uvicorn

import db
from db import *
from schemas import Item


app = FastAPI()

@app.get("/soldiers")
def get_all_soldiers():
    return get_all()


@app.post("/soldiers")
def post_soldier(body: Item):
    pass

@app.delete("/soldiers/{soldier_id}")
def delete_soldier(soldier_id: int):
    deleted = db.delete(soldier_id)
    return deleted





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3306)