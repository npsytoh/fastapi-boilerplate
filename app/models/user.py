from sqlalchemy import Column, Integer, String

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(20), index=True)
    email = Column(String, unique=True, index=True)
