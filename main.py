from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name:str
    email:str
    password:str
    
@app.post("/register")
async def registerUser(user: User):
    user.append(user.dict())
    return{"message":"Successfully registered user"}

@app.get("/users")
async def listUsers():
    return users