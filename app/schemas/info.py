from app.schemas.base import BaseSchema


class InfoResponse(BaseSchema):
    title: str
    version: str
