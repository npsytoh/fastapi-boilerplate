from sqlalchemy.orm import Session

from app import models, schemas


def create_user(db: Session, body: schemas.UserRequest) -> models.User:
    obj = models.User(user_name=body.user_name, email=body.email)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_all_users(db: Session):
    return db.query(models.User).all()
