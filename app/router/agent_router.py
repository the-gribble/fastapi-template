from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import database, schemas
from ..database.agent import crud as CrudAgent
from ..lib.agent.models import ContactModel
from ..lib.user.models import UserModel
from ..auth import get_validated_user, verify_token

router = APIRouter()

@router.get("/contact-read", response_model=List[ContactModel])
def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db), current_user: UserModel = Depends(get_validated_user)):
    contacts = CrudAgent.get_contacts(db, skip=skip, limit=limit)
    return contacts

@router.post("/contact-add", response_model=ContactModel)
def add_contact(contact: ContactModel, db: Session = Depends(database.get_db), current_user: UserModel = Depends(get_validated_user)):
    return CrudAgent.create_contact(db=db, contact=contact)

@router.delete("/contact-delete")
def delete_contact(contact_id: int, db: Session = Depends(database.get_db), current_user: UserModel = Depends(get_validated_user)):
    if CrudAgent.delete_contact(db=db, contact_id=contact_id):
        return {"message": "Contact deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Contact not found")

@router.put("/contact-update", response_model=ContactModel)
def update_contact(contact_id: int, contact: ContactModel, db: Session = Depends(database.get_db), current_user: UserModel = Depends(get_validated_user)):
    updated_contact = CrudAgent.update_contact(db=db, contact_id=contact_id, contact=contact)
    if updated_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated_contact