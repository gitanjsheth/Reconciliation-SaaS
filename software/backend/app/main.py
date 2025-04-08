# app/main.py
from fastapi import FastAPI
from app.api.user import router as user_router
from app.api.auth import router as auth_router

app = FastAPI()

# Correct router inclusions
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])