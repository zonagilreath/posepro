from pydantic import BaseModel, EmailStr, Field


class AuthRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    name: str | None = None


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_email: EmailStr
    message: str


class SessionResponse(BaseModel):
    authenticated: bool
    token_preview: str | None = None
