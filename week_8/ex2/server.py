from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel



class Item(BaseModel):
    type: str
    attributes: dict




app = FastAPI()

@app.post("/")
def post_data(data: dict):
    return data



if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8002)
