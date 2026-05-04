from fastapi import FastAPI 
from todos import router
import todos

app = FastAPI()


app.include_router(todos.router)

