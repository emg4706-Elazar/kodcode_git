from fastapi import FastAPI


all_items = {
    1: "banana" ,
    2: "apple"
}


app = FastAPI()


@app.get("/items")
def get_items():
    return all_items


# Query param
@app.get("/items")
def get_some_items(some: int = 0):
    if some:
        dicti = dict()




# Path param
@app.get("/items{item_id}")
def get_items(item_id: int):
    return all_items[item_id]
















