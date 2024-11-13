from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, schemas
from app.core.database import get_async_db

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[schemas.UserResponse])
async def get_users(db: AsyncSession = Depends(get_async_db)):
    return crud.get_all_users(db)


@router.post("/", response_model=schemas.UserResponse)
async def create_user(body: schemas.UserRequest, db: AsyncSession = Depends(get_async_db)):
    return crud.create_user(db, body)
