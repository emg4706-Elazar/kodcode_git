import uvicorn
from fastapi import FastAPI



app = FastAPI()


@app.get("/users/1")
def get_users():
    dicti = {
        "Name": "Leanne Graham",
        "Email": "Sincere@april.biz",
        "City": "Gwenborough"
    }
    return dicti

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
