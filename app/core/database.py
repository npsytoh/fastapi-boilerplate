from collections.abc import AsyncGenerator, Generator

from pytest import Session
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

database_url = URL.create(
    "postgresql",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.APP_HOST,
    database=settings.DB_NAME,
)


try:
    engine = create_engine(
        database_url,
        pool_pre_ping=True,
        echo=False,
        future=True,
    )
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    print(f"DataBase connection failed: {e}")


try:
    async_engine = create_async_engine(
        database_url,
        pool_pre_ping=True,
        echo=False,
        future=True,
    )
    async_session_local = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
except Exception as e:
    print(f"DataBase connection failed: {e}")


def get_db() -> Generator[Session, None, None]:
    try:
        db = session_local()
        yield db
    finally:
        db.close()


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_local() as db:
        try:
            yield db
        finally:
            await db.close()
