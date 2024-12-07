from fastapi import HTTPException


class APIException(HTTPException):
    def __init__(self, name: str):
        self.name = name
