from typing import Optional
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid

class Book(SQLModel, table=True):
    __tablename__ = "books"
    
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    title: str
    author: str
    publisher: str
    publisher_date: str
    page_count: int
    language: str
    createdAT: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updatedAT: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now, onupdate=datetime.now))

    def __repr__(self):
        print(f"Book {self.title}")
        return f"<Book {self.title}>"