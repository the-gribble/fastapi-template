from sqlalchemy import Column, String, BigInteger, text, Identity
from .database import Base, SessionLocal, engine
from sqlalchemy.schema import CreateTable

session = SessionLocal()  # This creates a session

# Could not get table auto-creation nor comments to work for some reason. 
# Also battled with getting column autoincrement working, Tried autoincrement, and Sequence. Both were ignored. Only Identity worked.

class UserSchema(Base):
    __tablename__ = "users"

    id = Column(BigInteger, Identity(start=1, always=True), primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)

# print(str(CreateTable(UserSchema.__table__)))  # Display the generated SQL

class ContactSchema(Base):
    __tablename__ = "contacts"

    id = Column(BigInteger, Identity(start=1, always=True), primary_key=True, index=True)
    full_name = Column(String, index=True)
    mobile_no = Column(String)
    email = Column(String)
    current_address = Column(String)

# print(str(CreateTable(ContactSchema.__table__)))  # Display the generated SQL

class Config:
        orm_mode = True  # This allows converting SQLAlchemy models to Pydantic models

# Get the create table statements for all tables in the metadata
create_statements = "\n".join(
    str(CreateTable(table)) for table in Base.metadata.sorted_tables
)

sql_file_path = "create_statements.sql"

with open(sql_file_path, "w") as f:
    f.write(create_statements)

# To display the generated SQL
print(create_statements)
