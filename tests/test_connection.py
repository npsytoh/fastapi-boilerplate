import asyncio

from sqlalchemy import URL, create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine


def test_connection():
    database_url = URL.create(
        "postgresql",
        username="postgres",
        password="pass",
        host="localhost",
        database="postgres",
    )

    engine = create_engine(
        database_url,
        pool_pre_ping=True,
        echo=False,
        future=True,
    )

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 'connection success'"))
        print(result.scalar())


async def test_async_connection():
    async_database_url = URL.create(
        "postgresql+asyncpg",
        username="postgres",
        password="pass",
        host="localhost",
        database="postgres",
    )

    async_engine = create_async_engine(
        async_database_url,
        pool_pre_ping=True,
        echo=False,
        future=True,
    )

    async with async_engine.connect() as connection:
        result = await connection.execute(text("SELECT 'async connection success'"))
        print(result.scalar())


test_connection()
asyncio.run(test_async_connection())
