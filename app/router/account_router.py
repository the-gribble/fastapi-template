from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import database, schemas
from ..database.user import crud as CrudUser
from ..lib.agent.models import ContactModel
from ..lib.user.models import UserAccessModel, UserModel
from ..auth import create_access_token

router = APIRouter()

@router.post("/acc-create")
def create_account(user: UserModel, db: Session = Depends(database.get_db)):
    db_user = CrudUser.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return CrudUser.create_user(db=db, user=user)

@router.post("/acc-login")
def login_for_access_token(form_data: UserAccessModel, db: Session = Depends(database.get_db)):
    user = CrudUser.get_user_by_username(db, username=form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # This is a simplified version of password checking, replace with actual hash verification in production
    if user.password != form_data.password + "notreallyhashed":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}