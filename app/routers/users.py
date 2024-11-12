from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[schemas.UserResponse])
async def get_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)


@router.post("/", response_model=schemas.UserResponse)
async def create_user(body: schemas.UserRequest, db: Session = Depends(get_db)):
    return crud.create_user(db, body)
