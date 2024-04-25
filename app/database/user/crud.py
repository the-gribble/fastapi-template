from sqlalchemy.orm import Session
from .. import schemas
from ...lib.user.models import UserAccessModel, UserModel

def get_user_by_username(db: Session, username: str):
    return db.query(schemas.UserSchema).filter(schemas.UserSchema.username == username).first()

def create_user(db: Session, user: UserModel):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = schemas.UserSchema(username=user.username, email=user.email, password=fake_hashed_password,
                   first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user