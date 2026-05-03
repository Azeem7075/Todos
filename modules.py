from database import Base, SessionLocal
from sqlalchemy import Column, String, Boolean, Integer


class Todos(Base):
    __tablename__= "todos"
    id = Column( Integer ,primary_key=True, index=True)
    text = Column (String)
    done = Column(Boolean,default=False)


def dependency():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


