from fastapi import FastAPI 
from todos import router as todo_router
from auth import router as auth_router

app = FastAPI()






app.include_router(todo_router)
app.include_router(auth_router)





































