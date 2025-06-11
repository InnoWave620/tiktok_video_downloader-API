from pydantic import BaseModel, HttpUrl
from typing import Optional, List

class FormatRequest(BaseModel):
    url: HttpUrl

class FormatInfo(BaseModel):
    format_id: str
    ext: str
    resolution: str
    filesize: Optional[int]

class FormatResponse(BaseModel):
    title: str
    formats: List[FormatInfo]

class DownloadRequest(FormatRequest):
    format_id: str
