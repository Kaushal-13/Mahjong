from fastapi import FastAPI
from routers.chat import chat_router
from routers.room import rooms_router
from db.database import init_db

app = FastAPI()
init_db()

app.include_router(chat_router)
app.include_router(rooms_router)