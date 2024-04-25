from sqlalchemy.orm import Session
from . import schemas
# from .models import UserType, ContactType
from ..lib.agent.models import ContactModel
from ..lib.user.models import UserCreateModel, UserModel

def get_user_by_username(db: Session, username: str):
    return db.query(UserCreateModel).filter(UserCreateModel.username == username).first()

def create_user(db: Session, user: schemas.User):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = UserModel(username=user.username, email=user.email, password=fake_hashed_password,
                   first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ContactModel).offset(skip).limit(limit).all()

def create_contact(db: Session, contact: schemas.Contact):
    db_contact = ContactModel(name=contact.name, mobile=contact.mobile_no, email=contact.email, address=contact.current_address)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contact(db: Session, contact_id: int):
    return db.query(ContactModel).filter(ContactModel.id == contact_id).first()

def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(ContactModel).filter(ContactModel.id == contact_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
        return True
    return False

def update_contact(db: Session, contact_id: int, contact: schemas.Contact):
    db_contact = db.query(ContactModel).filter(ContactModel.id == contact_id).first()
    if db_contact:
        db_contact.name = contact.name
        db_contact.mobile = contact.mobile_no
        db_contact.email = contact.email
        db_contact.address = contact.current_address
        db.commit()
        db.refresh(db_contact)
        return db_contact
    return None