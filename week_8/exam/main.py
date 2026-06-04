import uvicorn
from fastapi import FastAPI, HTTPException
from weapons_manager import *
from pydantic import BaseModel
from logging_config import logger



class Item(BaseModel):
    type: str
    model: str
    ammo_type: str
    condition: str




app = FastAPI()
manager = WeaponsManager()
logger.info("Server start")


@app.get("/weapons")
def get_all_weapons():
    logger.info("get shapes")
    return manager.get_weapons()


@app.post("/weapons")
def post_weapon(body: Item):
    logger.info("post weapon started")
    new_id = manager.get_new_id()
    new_weapon = body.model_dump()
    new_weapon["id"] = new_id
    try:
        manager.create_weapon(new_weapon)
        logger.info("post weapon wes success")
        return f"A new weapon was created successfully. Its id is {new_id}"
    except Exception as e:
        logger.warning("post weapon failed")
        raise HTTPException(status_code=422,
                            detail=f"The post process failed, {e}")



@app.put("/weapon/{id}")
def put_weapon(id: int, new_data: Item):
    logger.info("put weapon started")
    # Check if id is existed
    if not manager.get_one_weapon(id):
        logger.warning("put weapon failed. wrong id")
        raise HTTPException(status_code=404,
                            detail=f"id '{id}' is not found")
    try:
        updated_weapon = new_data.model_dump()
        updated_weapon["id"] = id
        manager.update_weapon(updated_weapon)
        logger.error("put weapon was success")
        return f"weapon '{id}' was updated successfully'"
    except Exception as e:
        logger.error("put weapon failed. known error")
        raise HTTPException(status_code=422,
                            detail=f"The put process failed, {e}")


@app.delete("/weapon/{id}")
def delete_weapon(id: int):
    logger.info("delete weapon started")
    # Check if id is existed
    if not manager.get_one_weapon(id):
        logger.warning("delete weapon failed. wrong id")
        raise HTTPException(status_code=404,
                            detail=f"id '{id}' is not found")
    try:
        manager.delete_weapon(id)
        logger.info("deleted shape was successfully")
        return "deleted shape was successfully"
    except Exception as e:
        logger.error("delete weapon failed. known error")
        raise HTTPException(status_code=422,
                            detail=f"The delete process failed, {e}")


@app.get("/weapons/by-condition")
def get_weapons_by_condition(condition: str):
    logger.info("get weapons_by condition started")
    try:
        sorted_weapons = manager.get_by_cond(condition)
        logger.info("get weapons by condition was success")
        return sorted_weapons
    except KeyError:
        raise HTTPException(status_code=404,
                            detail=f"Process failed. '{condition}' condition, not found")

    except Exception as e:
        raise HTTPException(status_code=422,
                            detail=f"GET request failed. {e}")




@app.get("/weapons/{id}")
def get_weapon_by_id(id: int):
    weapon = manager.get_one_weapon(id)
    if weapon:
        return weapon

    raise HTTPException(status_code=404,
                        detail=f"This id is not found")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
