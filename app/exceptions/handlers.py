from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

async def file_not_found_exception_handler(request: Request, exc: FileNotFoundError):
    logger.error(f"File not found: {exc}")
    return JSONResponse(
        status_code=404,
        content={"detail": "Requested file was not found on the server."},
    )
