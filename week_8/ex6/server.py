from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel



app = FastAPI()

class CircleAttributes(BaseModel):
    quoter: float
    radius: float

class SquareAttributes(BaseModel):
    side: float


class RectangleAttributes(BaseModel):
    length: float
    width: float


class Item(BaseModel):
    type: str
    attributes: RectangleAttributes | SquareAttributes | CircleAttributes


@app.post("/shapes")
def post_shape(shape : Item):

    new_id = get_new_id()
    new_shape = shape.model_dump()


    new_shape["attributes"]["_id"] = new_id
    manager.create_shape(new_shape)
    manager.save_to_json()

    return f"new shape was created"