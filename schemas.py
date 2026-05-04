from pydantic import BaseModel, Field, EmailStr


class TodoSchema(BaseModel):
    text : str
    done : bool

    
class UserSchema(BaseModel):
    user_name : str = Field(min_length=3,max_length=20)
    email: EmailStr
    password: str = Field(min_length=1, max_length=72)
    first_name : str = Field(max_length=10)
    second_name: str = Field (max_length=10)
    role  : str = Field( default="user")












