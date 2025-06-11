from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_formats_invalid_url():
    resp = client.post("/api/video/formats", json={"url": "not a url"})
    assert resp.status_code == 422
