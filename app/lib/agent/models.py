from pydantic import BaseModel

class ContactModel(BaseModel):
    id: int
    full_name: str
    mobile_no: str
    email: str
    current_address: str