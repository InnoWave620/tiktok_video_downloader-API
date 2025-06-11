import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.schemas.video import FormatRequest, FormatResponse, DownloadRequest
from app.services.video_service import extract_formats, download_format

router = APIRouter()

@router.post("/formats", response_model=FormatResponse)
async def get_formats(req: FormatRequest):
    try:
        title, fmts = extract_formats(req.url)
    except Exception as e:
        raise HTTPException(400, detail=str(e))
    return {"title": title, "formats": fmts}

@router.post("/download")
async def download(req: DownloadRequest):
    try:
        fpath = download_format(req.url, req.format_id)
    except Exception as e:
        raise HTTPException(500, detail=str(e))
    return FileResponse(fpath, filename=os.path.basename(fpath))
