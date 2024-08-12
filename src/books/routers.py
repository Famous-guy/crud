from typing import List
from fastapi import APIRouter, status
from src.books.books_data import books
from src.books.schemas import Book, BookUpdate
from fastapi.exception_handlers import HTTPException

book_router = APIRouter()


@book_router.get("/", response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_books():
    return books


@book_router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_books(create_book: Book) -> dict:
    new_book = create_book.model_dump()
    books.append(new_book)
    return new_book


@book_router.get("/{book_id}")
async def patch_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book Id not found"
    )


@book_router.patch("/{book_id}", response_model=Book)
async def update_book(book_id: int, update_book: BookUpdate) -> Book:
    for book in books:
        if book["id"] == book_id:
            if update_book.title is not None:
                book["title"] = update_book.title
            if update_book.publisher is not None:
                book["publisher"] = update_book.publisher
            if update_book.page_count is not None:
                book["page_count"] = update_book.page_count
            if update_book.language is not None:
                book["language"] = update_book.language
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book Id not found"
    )


@book_router.delete("/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book Id not found"
    )
