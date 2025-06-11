from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.video import router as video_router
from app.config import settings
from app.exceptions.handlers import file_not_found_exception_handler

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(video_router, prefix="/api/video")

app.add_exception_handler(FileNotFoundError, file_not_found_exception_handler)
