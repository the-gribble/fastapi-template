from .config import Settings
from fastapi import Header, HTTPException
from fastapi.param_functions import Depends

def get_settings():
    return 

async def verify_token(token: str = Header(...), settings: Settings = Depends(get_settings)):
    if token != settings.AUTH_TOKEN:
        raise HTTPException(status_code=400, detail="Invalid token")