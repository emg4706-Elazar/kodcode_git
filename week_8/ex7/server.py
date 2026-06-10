from fastapi import FastAPI
import uvicorn
from logger import logger

app = FastAPI()

@app.get("/store")
def purchase(username, item, price):
    logger.info(f"{username} started to buy {item}")

    if int(price) < 0:
        logger.error(f"The price is less than 0")
        return f"The price is less than 0"
    if int(price) > 1000:
        logger.warning(f"The price is more than 1000")
        return f"The price is more than 1000"

    logger.info(f"The purchase completed was successfully")
    return f"The purchase was completed successfully"








if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8004, reload=True)

