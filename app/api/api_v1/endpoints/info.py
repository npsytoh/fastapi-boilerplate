from fastapi import APIRouter

from app import schemas
from app.core.config import settings

router = APIRouter(prefix="/info", tags=["info"])


@router.get("/", tags=["info"], response_model=schemas.InfoResponse)
async def get_info() -> dict[str, str]:
    return {"title": settings.PROJECT_NAME, "version": settings.VERSION}
