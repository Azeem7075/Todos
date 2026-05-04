from database import Base, SessionLocal
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey


class Todos(Base):
    __tablename__= "todos"
    id = Column( Integer ,primary_key=True, index=True)
    text = Column (String)
    done = Column(Boolean,default=False)
    owner_id = Column(Integer , ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True, index=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    second_name = Column(String)
    role = Column(String)



def dependency():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


