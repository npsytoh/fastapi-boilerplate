from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app import models, schemas


async def create_user(db: AsyncSession, body: schemas.UserRequest) -> models.User:
    obj = models.User(user_name=body.user_name, email=body.email)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get_all_users(db: AsyncSession):
    result = await db.execute(select(models.User))
    return result.scalars().all()
