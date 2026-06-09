from fastapi import FastAPI
from dal.animal_dal import *


app = FastAPI()
animal_dal = AnimalDAL()

@app.get("/animals")
def get_all_animals():
    return animal_dal.get_animals()


@app.post("/animals")
def create_animal(name: str, type_animal: str, age: int):
    return animal_dal.create_animal(name, type_animal, age)
