from app.schemas.auth import AuthRequest, AuthResponse, SessionResponse


class AuthService:
    """Thin auth stub that preserves the API contract while real auth is pending."""

    def register(self, payload: AuthRequest) -> AuthResponse:
        return AuthResponse(
            access_token=f"dev-register-token-{payload.email}",
            user_email=payload.email,
            message="Stub register endpoint. Replace with Supabase Auth or JWT issuance.",
        )

    def login(self, payload: AuthRequest) -> AuthResponse:
        return AuthResponse(
            access_token=f"dev-login-token-{payload.email}",
            user_email=payload.email,
            message="Stub login endpoint. Replace with real credential validation.",
        )

    def validate_session(self, authorization: str | None) -> SessionResponse:
        if not authorization:
            return SessionResponse(authenticated=False, token_preview=None)

        token_preview = authorization[:24]
        return SessionResponse(authenticated=True, token_preview=token_preview)
