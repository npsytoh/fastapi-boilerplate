from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

try:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        pool_pre_ping=True,
        echo=False,
        future=True,
    )
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    print(f"Connection failed: {e}")


def get_db() -> Generator:
    try:
        db = session_local()
        yield db
    finally:
        db.close()
