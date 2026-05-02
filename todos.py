from fastapi import FastAPI, Depends
from database import Base, SessionLocal , engine 
from modules import Todos , dependency
from sqlalchemy.orm import Session

app = FastAPI()


Base.metadata.create_all(bind = engine)

@app.post("/")
def insertit(data:str, db:Session = Depends(dependency)):
    test = Todos(text = data)
    db.add(test)
    db.commit()


@app.get("/")
def see_all(db:Session = Depends(dependency)):
    data = db.query(Todos).all()
    return data


@app.get("/by_id")
def get_by_id(id:int, db:Session = Depends(dependency)):
    data = db.query(Todos).filter(Todos.id == id).first()
    return data

@app.put("/")
def update(id:int, text:str,db:Session = Depends(dependency)):
    data = db.query(Todos).filter(Todos.id== id).first()
    data.text = text
    db.add(data)
    db.commit()
