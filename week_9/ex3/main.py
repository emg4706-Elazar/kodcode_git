from fastapi import FastAPI
from fastapi.params import Query
from queries import *
import uvicorn


app = FastAPI()


@app.get("/soldiers")
def get_soldiers(
        rank: str | None = Query(default=None),
        sort: str | None = Query(default="asc"),
        unit: str | None = Query(default=None)
    ):
    if rank:
        rows = get_by_rank(rank)
        return rows
    elif unit:
        rows = get_by_unit(unit)
        return rows
    return get_active_sorted(sort)


@app.get("/soldiers/units")
def get_units():
    return {"units": get_distinct_units()}


@app.get("/soldiers/search")
def search_soldiers(name: str = Query(...)):
    return {"soldiers": search_by_name(name)}

@app.get("/soldiers/missing-rank")
def get_miss_rank():
    return {"soldiers": get_missing_rank()}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)




