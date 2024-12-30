from uuid import uuid4

import sys
sys.path.append("..")
from dao.room_dao import create_room

import sys
sys.path.append("..")
from db.database import SessionLocal

def create_new_room():
    db = SessionLocal()
    db_room = create_room(db, str(uuid4()))
    db.close()

    return {
            "room_id": db_room.id,
            "room_name": db_room.name,
            "message": "Room Created",
            }