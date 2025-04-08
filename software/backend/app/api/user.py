# app/api/user.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import user as user_model
from app.schemas import user as user_schema
from app.db.database import get_db
from uuid import UUID
from app.utils.auth import get_current_user
from app.models.user import User
from app.utils.auth import hash_password

router = APIRouter(
    tags=["Users"]
)

@router.post("/", response_model=user_schema.UserOut)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    
    existing_user = db.query(user_model.User).filter(user_model.User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered, kindly login."
        )
    
    existing_phone = db.query(user_model.User).filter(user_model.User.phone_number == user.phone_number).first()
    if existing_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="Phone number already registered, use another."
        )
    
    hashed_password = hash_password(user.password)
    
    new_user = user_model.User(
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        hashed_password=hashed_password,
        role="admin",  # Or handle dynamically
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get("/", response_model=list[user_schema.UserOut])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(user_model.User).offset(skip).limit(limit).all()
    return users

@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return {
        "public_id": current_user.public_id,
        "name": current_user.name,
        "email": current_user.email,
        "phone_number": current_user.phone_number,
        "role": current_user.role
    }

@router.get("/{public_id}", response_model=user_schema.UserOut)
def get_user(public_id: UUID, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.public_id == public_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.delete("/{public_id}", response_model=dict)
def delete_user(public_id: UUID, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.public_id == public_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}