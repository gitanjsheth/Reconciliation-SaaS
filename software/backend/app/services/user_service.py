from sqlalchemy.ext.asyncio import AsyncSession
from app.db import crud
from app.schemas.user import UserCreate

async def register_new_user(db: AsyncSession, user_in: UserCreate):
    existing_user = await crud.get_user_by_email(db, user_in.email)
    if existing_user:
        raise ValueError("User already exists")
    return await crud.create_user(db, user_in)

async def authenticate_existing_user(db: AsyncSession, email: str, password: str):
    user = await crud.authenticate_user(db, email, password)
    if not user:
        raise ValueError("Invalid credentials")
    return user