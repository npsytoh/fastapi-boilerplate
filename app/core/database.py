from collections.abc import AsyncGenerator, Generator

from pytest import Session
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


def get_database_url(is_async: bool = False) -> str:
    database_driver = "postgresql"

    if is_async:
        database_driver += "+asyncpg"
    else:
        database_driver += "+psycopg2"

    url_object = URL.create(
        drivername=database_driver,
        username=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.APP_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
    )
    return url_object.render_as_string(hide_password=False)


try:
    engine = create_engine(
        get_database_url(),
        pool_pre_ping=True,
        echo=False,
        future=True,
    )
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    raise ValueError(f"DataBase connection failed: {e}")


try:
    async_engine = create_async_engine(
        get_database_url(is_async=True),
        pool_pre_ping=True,
        echo=False,
        future=True,
    )
    async_session_local = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
except Exception as e:
    raise ValueError(f"DataBase connection failed: {e}")


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
