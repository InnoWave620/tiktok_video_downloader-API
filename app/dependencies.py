from fastapi import Depends
from app.config import settings

def get_settings():
    return settings

# Example for future use (e.g., authentication)
def verify_token_header(token: str = Depends(...)):
    if token != "expected-token":
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail="Invalid token")
