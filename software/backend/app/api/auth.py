from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import User
from app.utils.auth import verify_password, create_access_token, get_current_user
from app.db.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_user)):
        return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role
    }