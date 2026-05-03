from fastapi import FastAPI, Depends
from database import Base, SessionLocal , engine 
from modules import Todos , dependency
from sqlalchemy.orm import Session
from schemas import TodoSchema

app = FastAPI()


Base.metadata.create_all(bind = engine)

@app.post("/")
def insertit(data:TodoSchema, db:Session = Depends(dependency)):
    test = Todos(text = data.text)
    db.add(test)
    db.commit()


@app.get("/")
def see_all(db:Session = Depends(dependency)):
    data = db.query(Todos).all()
    return data


@app.get("/get_id/{id}")
def get_by_id(id:int, db:Session = Depends(dependency)):
    data = db.query(Todos).filter(Todos.id == id).first()
    return data


@app.put("/{id}")
def update(id:int, data:TodoSchema,db:Session = Depends(dependency)):
    store = db.query(Todos).filter(Todos.id== id).first()
    store.text = data.text
    db.commit()

@app.delete("/{id}")
def delete(id:int, db: Session = Depends(dependency)):
    store = db.query(Todos).filter(Todos.id == id).first()
    db.delete(store)
    db.commit()

 