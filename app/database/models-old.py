from pydantic import BaseModel

class UserType(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str

class ContactType(BaseModel):
    name: str
    mobile_no: str
    email: str
    current_address: str