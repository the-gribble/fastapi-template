from sqlalchemy.orm import Session
from .. import schemas
# from .models import UserType, ContactType
# from ...lib.agent.models import ContactModel
from ..schemas import ContactSchema

def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ContactSchema).offset(skip).limit(limit).all()

def create_contact(db: Session, contact: ContactSchema):
    db_contact = ContactSchema(full_name=contact.full_name, mobile_no=contact.mobile_no, email=contact.email, current_address=contact.current_address)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contact(db: Session, contact_id: int):
    return db.query(ContactSchema).filter(ContactSchema.id == contact_id).first()

def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(ContactSchema).filter(ContactSchema.id == contact_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
        return True
    return False

def update_contact(db: Session, contact_id: int, contact: ContactSchema):
    db_contact = db.query(ContactSchema).filter(ContactSchema.id == contact_id).first()
    if db_contact:
        db_contact.full_name = contact.full_name
        db_contact.mobile_no = contact.mobile_no
        db_contact.email = contact.email
        db_contact.current_address = contact.current_address
        db.commit()
        db.refresh(db_contact)
        return db_contact
    return None