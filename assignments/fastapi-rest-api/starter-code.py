# Starter code for FastAPI REST API assignment

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI API!"}

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

# To run: uvicorn starter-code:app --reload
