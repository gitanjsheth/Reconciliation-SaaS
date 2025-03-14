from pydantic import BaseModel, EmailStr, validator

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str  # Keep as str to preserve leading 0 if any
    password: str

    @validator('phone_number')
    def validate_phone_number(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits.')
        if len(v) != 10:
            raise ValueError('Phone number must be exactly 10 digits long.')
        return v

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: str  # Display it with +91 added in the UI, not in DB
    role: str
    is_active: bool

    class Config:
        from_attributes = True