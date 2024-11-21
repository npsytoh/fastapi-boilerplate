from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, schemas
from app.core.database import get_async_db

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[schemas.UserResponse])
async def get_all_users(db: AsyncSession = Depends(get_async_db)):
    return await crud.get_all_users(db)


@router.get("/{id}", response_model=schemas.UserResponse)
async def get_user(id: int, db: AsyncSession = Depends(get_async_db)):
    return await crud.get_user_by_id(db, id=id)


@router.post("/", response_model=schemas.UserResponse)
async def create_user(body: schemas.UserRequest, db: AsyncSession = Depends(get_async_db)):
    return await crud.create_user(db, body)


@router.delete("/{id}")
async def delete_user(id: int, db: AsyncSession):
    await crud.delete_user(db, id=id)
