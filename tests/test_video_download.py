# tests/test_video_download.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_download_missing_format():
    """
    This test ensures that the /download endpoint returns a 422
    when the 'format_id' field is missing or empty.
    """
    response = client.post(
        "/api/video/download",
        json={
            "url": "https://www.tiktok.com/@user/video/1234567890",
            "format_id": ""
        }
    )
    assert response.status_code == 422
