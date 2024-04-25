from pydantic import BaseModel

class UserAccessModel(BaseModel):
    username: str
    password: str

class UserModel(BaseModel):
    id:int
    username: str
    email: str
    password: str
    first_name: str
    last_name: str