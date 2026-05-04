from fastapi import FastAPI, Depends, APIRouter
from database import Base,  engine 
from modules import Todos , dependency
from sqlalchemy.orm import Session
from schemas import TodoSchema



router = APIRouter()


Base.metadata.create_all(bind = engine)

@router.post("/", status_code= 201)
def insertit(data:TodoSchema, db:Session = Depends(dependency)):
    test = Todos(text = data.text)
    db.add(test)
    db.commit()
    return  test


@router.get("/", status_code= 200)
def see_all(db:Session = Depends(dependency)):
    data = db.query(Todos).all()
    return data


@router.get("/get_id/{id}", status_code= 200)
def get_by_id(id:int, db:Session = Depends(dependency)):
    data = db.query(Todos).filter(Todos.id == id).first()
    return data
    


@router.put("/{id}", status_code= 200)
def update(id:int, data:TodoSchema,db:Session = Depends(dependency)):
    store = db.query(Todos).filter(Todos.id== id).first()
    store.text = data.text
    db.commit()
    return "todo had been updated"

@router.delete("/{id}", status_code=204)
def delete(id:int, db: Session = Depends(dependency)):
    store = db.query(Todos).filter(Todos.id == id).first()
    db.delete(store)
    db.commit()
   

 