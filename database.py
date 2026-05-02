from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker, declarative_base

link = "sqlite:///./todos.db"

engine = create_engine(
    link,
    connect_args={
        "check_same_thread" :False
    }
)

SessionLocal = sessionmaker(
    bind= engine
)

Base = declarative_base()

