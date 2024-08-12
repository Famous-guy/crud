from fastapi import FastAPI
from src.books.routers import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db
@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"Server is starting...")
    await init_db()
    yield
    print(f"Server has Stopped!")
version = "v1"

app = FastAPI(
    lifespan=life_span,
    title="Books API",
    version=version,
    description="A Rest API for our Book Review Web Service",
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["Books"])
