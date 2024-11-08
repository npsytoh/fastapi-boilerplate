from pydantic import EmailStr

from app.schemas.base import BaseSchema


class UserParams(BaseSchema):
    user_name: str
    email: EmailStr
    password: str


class UserResponse(UserParams):
    pass
