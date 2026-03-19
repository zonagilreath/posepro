from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import get_settings
from app.routers.auth import router as auth_router
from app.routers.health import router as health_router
from app.routers.proposals import router as proposals_router

settings = get_settings()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.cors_origins.split(",") if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix=settings.api_prefix)
app.include_router(auth_router, prefix=settings.api_prefix)
app.include_router(proposals_router, prefix=settings.api_prefix)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": settings.app_name,
        "environment": settings.app_env,
        "docs": "/docs",
        "health": f"{settings.api_prefix}/health",
        "auth": f"{settings.api_prefix}/auth",
        "proposal_preview": f"{settings.api_prefix}/proposals/generate/preview",
        "proposal_stream": f"{settings.api_prefix}/proposals/generate",
        "proposal_preview_note": "POST JSON to preview and stream endpoints",
    }
