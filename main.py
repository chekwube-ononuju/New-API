
from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def read_root():
    return {"message": "My name is Chekwube"}

@app.get("/items")
def read_items():
    return items

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return {"item": item, "message": "Item added successfully!"}
