from fastapi import APIRouter, HTTPException
from .crud import create_user, get_users, get_user
from .schemas import UserCreate, UserRead

router = APIRouter()

@router.post("/users/")
async def create_user_endpoint(user: UserCreate):
    return create_user(db, user)

@router.get("/users/")
async def read_users():
    return get_users(db)

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    return get_user(db, user_id)