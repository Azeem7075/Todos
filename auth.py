from passlib.context import CryptContext
from fastapi import APIRouter, Depends
from modules import dependency, User
from sqlalchemy.orm import Session
from schemas import UserSchema



router = APIRouter(prefix="/user")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/")
def create_user(data:UserSchema, db:Session = Depends(dependency)):
    hashed_password = bcrypt_context.hash(data.password)

    data = User(user_name = data.user_name,
    email = data.email,
    password = hashed_password,
    first_name = data.first_name,
    second_name = data.second_name,
    role  = data.role )
    db.add(data)
    db.commit()




    """
    class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True, index=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    second_name = Column(String)
    role = Column(String)"""


    """
    class UserSchema(BaseModel):
    user_name : str = Field(min_length=3,max_length=20)
    email: EmailStr
    password: str = Field(min_length=1)
    first_name : str = Field(max_length=10)
    second_name: str = Field (max_length=10)
    role  : str = Field( default="user")
"""
