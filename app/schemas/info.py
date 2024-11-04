from pydantic import BaseModel


class InfoResponse(BaseModel):
    title: str
    version: str
