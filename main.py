from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#Path Parameters: Get an Item by ID

class Item(BaseModel):
    item_id: str
    item_value: str

dict = {}

@app.get("/items/{item_id}")
async def get_item(item_id:str):
    if item_id not in dict:
        raise HTTPException(status_code=409, detail=f'Item with id {item_id} doesn''t exist')
    return dict[item_id]

#POST item
@app.post("/items/")
def create_item(item: Item) -> Item:
    print("got here")
    if item.item_id in dict:
        raise HTTPException(status_code=409, detail=f'Item with id {item.item_id} already exists')
    dict[item.item_id] = item
    return item


#POST operation

class Book(BaseModel):
    isbn: int
    title: str

books = []

@app.post("/books/")
def create_book(book: Book) -> Book:
    if book in books:
        raise HTTPException(status_code=409, detail=f'Book with isbn {book.isbn} already exists')
    books.append(book)
    return book

