from datetime import datetime, timedelta
# from jose import JWTError, jwt
import jwt  # JWT library for creating and decoding tokens
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.orm import Session
from .database.database import get_db
# from .database.models import UserType
from .database.user.crud import get_user_by_username

SECRET_KEY = "4e6f9fba2b3720d2b7653a49c9a4fbe931abb072945c4d3d875b9a3e4f38b9b7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20160 # 14 days

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
security = HTTPBearer()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
# just verify the access token without the overhead of a DB call to check user access
def verify_token(credentials: str = Depends(security)):
    token = credentials.credentials
    print(token)
    try:
        # Decode the JWT token and check claims, expiration, etc.
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Additional checks can be done here, e.g., user permissions
        return payload  # Return decoded information
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

'''
Validate access token and return the validated user record for further use in API calls.

This has the added overhead of making a user call for every API call. 
'''
async def get_validated_user(credentials: str = Depends(security), db: Session = Depends(get_db)):
# async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):  
    token = credentials.credentials

    # credentials_exception = HTTPException(
    #     status_code=status.HTTP_401_UNAUTHORIZED,
    #     detail="Could not validate credentials",
    #     headers={"WWW-Authenticate": "Bearer"},
    # )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        username: str = payload.get("sub")
        if username is None:
            # raise credentials_exception
            raise HTTPException(status_code=401, detail="Invalid username (Get Current User)")
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired (Get Current User)")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token (Get Current User)")
    
    user = get_user_by_username(db, username=username)
    if user is None:
        # raise credentials_exception
        raise HTTPException(status_code=401, detail="Username does not exist (Get Current User)")
    
    return user