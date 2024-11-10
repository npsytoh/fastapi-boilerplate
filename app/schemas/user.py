from pydantic import EmailStr

from app.schemas.base import BaseSchema


class UserParams(BaseSchema):
    user_name: str
    email: EmailStr


class UserResponse(UserParams):
    pass
