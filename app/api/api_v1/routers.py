from fastapi import APIRouter

from app.api.api_v1.endpoints import info, users

router = APIRouter()

router.include_router(info.router)
router.include_router(users.router)
