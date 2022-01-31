from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#Path Parameters: Get an Item by ID
dict = {"obj1":"val1", "obj2":"val2"}

@app.get("/items/{item_id}")
async def get_item(item_id:str):
    return dict[item_id]

#POST operation

class Book(BaseModel):
    isbn: int
    title: str

books = []

@app.post("/books/")
def create_book(book: Book) -> Book:
    print("got here")
    if book in books:
        raise HTTPException(status_code=409, detail=f'Book with isbn {book.isbn} already exists')
    books.append(book)
    return book

