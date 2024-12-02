from pydantic import EmailStr

from app.schemas.base import BaseSchema


class UserBase(BaseSchema):
    user_name: str
    email: EmailStr


class UserUpdate(UserBase):
    user_name: str | None = None
    email: EmailStr | None = None


class UserRequest(UserBase):
    pass


class UserResponse(UserBase):
    pass

    class Config:
        orm_mode = True
