from fastapi import FastAPI
from app.api.user import router as user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Reconciliation SaaS Backend is running!"}