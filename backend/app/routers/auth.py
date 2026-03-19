from fastapi import APIRouter, Header

from app.schemas.auth import AuthRequest, AuthResponse, SessionResponse
from app.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])
auth_service = AuthService()


@router.post("/register", response_model=AuthResponse)
def register(payload: AuthRequest) -> AuthResponse:
    return auth_service.register(payload)


@router.post("/login", response_model=AuthResponse)
def login(payload: AuthRequest) -> AuthResponse:
    return auth_service.login(payload)


@router.get("/session", response_model=SessionResponse)
def validate_session(authorization: str | None = Header(default=None)) -> SessionResponse:
    return auth_service.validate_session(authorization)
