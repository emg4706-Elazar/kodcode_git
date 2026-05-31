from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello Elazar"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item number {item_id}"}

@app.get("/items/count")
def count_items():
    return {"count": 0}






if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)