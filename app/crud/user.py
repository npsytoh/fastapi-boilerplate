from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app import models, schemas


async def get_all_users(db: AsyncSession):
    result = await db.execute(select(models.User))
    return result.scalars().all()


async def get_user_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(models.User).where(models.User.id == id))
    return result.scalars().first()


async def create_user(db: AsyncSession, body: schemas.UserRequest) -> models.User:
    obj = models.User(user_name=body.user_name, email=body.email)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def delete_user(db: AsyncSession, id: int) -> None:
    user = await db.get(models.User, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await db.delete(user)
    await db.commit()
