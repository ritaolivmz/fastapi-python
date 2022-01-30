from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#Path Parameters: Get an Item by ID
dict = {"obj1":"val1", "obj2":"val2"}

@app.get("/items/{item_id}")
async def get_item(item_id:str):
    return dict[item_id]
