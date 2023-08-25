from fastapi import FastAPI
from pydantic import BaseModel
from calculator import cal1

class user_input(BaseModel):
    operation:str
    x:int
    y:float
app=FastAPI()

@app.post("/calculate")
def cal(item:user_input):
    result=cal1(item.operation,item.x,item.y)
    return result
