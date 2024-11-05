from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_user(user_name: str):
    return {"user_name": user_name}
