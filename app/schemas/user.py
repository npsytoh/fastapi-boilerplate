from pydantic import EmailStr

from app.schemas.base import BaseSchema


class UserParams(BaseSchema):
    user_name: str
    email: EmailStr


class UserRequest(UserParams):
    pass


class UserResponse(UserParams):
    pass

    class Config:
        orm_mode = True
