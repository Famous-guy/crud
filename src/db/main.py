from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import config

engine = AsyncEngine(
    create_engine(
        url=config.DATABASE_URL,
        echo=True
    )
)

async def init_db():
    async with engine.begin() as conn:
        try:
            await conn.run_sync(SQLModel.metadata.create_all)
            print("Tables created successfully!")
            print("Tables created successfully!")
        except Exception as e:
            print(f"Error creating tables: {e}")