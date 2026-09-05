from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}


items = {"foo": "The Foo Wrestlers" ,
    "how": "the love of world" ,
    "metallica": "hard death"}

@app.get("/items/{item_id}")
def read_item(item_id:str):
    return {item_id: items[item_id]}


@app.put("/items/{item_id}")
def create_item(item_id: str, item_name: str):
    items[item_id] = item_name
    return {item_id: items[item_id]}
