import uvicorn
from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

@app.get("/")
def home():
    return {"service": "my-api", "version": "1.0"}


@app.get("/users/admin")
def admin():
    return {"role": "admin", "access": "full"}


@app.get("/users/{user_id}")
def user(user_id):
    dicti = {
        "user_id": user_id,
        "name": "Elazar",
        "email": "emg4706@gmail.com"
    }
    return dicti


@app.get("/calc/{a}/{op}/{b}")
def calculate(a,op,b):
    dict_functions = {
        "add": lambda c, d: c+d,
        "sub": lambda c, d: c-d,
        "mul": lambda c, d: c*d,
        "div": lambda c, d: c/d
    }
    try:
        result = dict_functions[op](int(a), int(b))
        return {"operation": op, "result": result}
    except ZeroDivisionError as e:
        return "ZeroDivisionError"


@app.get("/status")
def status():
    sys_info = {
        "server name": "calculate",
        "time": datetime.now()
    }
    return sys_info




if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1", port=8000,reload=True)