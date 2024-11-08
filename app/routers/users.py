from typing import Annotated

from fastapi import APIRouter, Query

from app.schemas.user import UserParams, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=UserResponse)
async def get_user(params: Annotated[UserParams, Query()]):
    return params.model_dump(by_alias=True)
