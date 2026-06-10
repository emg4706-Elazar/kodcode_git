


# main.py
from fastapi import FastAPI, HTTPException
app = FastAPI()
# In-memory store for demonstration
items = {"1": "apple", "2": "banana"}
@app.get("/items/{item_id}")
def get_item(item_id: str):
# 404 — resource does not exist
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

    return {"id": item_id, "name": items[item_id]}


@app.post("/items/{item_id}")
def create_item(item_id: str, body: dict):
    # 409 — resource already exists
    if item_id in items:
        raise HTTPException(status_code=409, detail=f"Item {item_id} already exists")

    # 400 — missing required field
    if "name" not in body:
        raise HTTPException(status_code=400, detail="Field 'name' is required")

    items[item_id] = body["name"]
    return {"id": item_id, "name": body["name"]}