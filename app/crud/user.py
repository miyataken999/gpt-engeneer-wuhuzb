from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, UserRead

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, password=user.password, profile=user.profile, team_id=user.team_id, tags=user.tags)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()