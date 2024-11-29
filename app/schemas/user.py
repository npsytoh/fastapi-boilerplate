from pydantic import EmailStr

from app.schemas.base import BaseSchema


class UserBase(BaseSchema):
    user_name: str
    email: EmailStr


class UserRequest(UserBase):
    pass


class UserUpdate(UserBase):
    user_name: str | None = None
    email: str | None = None


class UserResponse(UserBase):
    pass

    class Config:
        orm_mode = True
