from pydantic import BaseModel, EmailStr, validator
from uuid import UUID

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    password: str

    @validator('phone_number')
    def validate_phone_number(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits.')
        if len(v) != 10:
            raise ValueError('Phone number must be exactly 10 digits long.')
        return v

class UserOut(BaseModel):
    public_id: UUID
    name: str
    email: EmailStr
    phone_number: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True