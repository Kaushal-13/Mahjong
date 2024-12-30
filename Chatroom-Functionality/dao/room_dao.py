from sqlalchemy.orm import Session

import sys
sys.path.append("..")
from models.room_model import RoomDB

def create_room(db: Session, name: str):
    db_room = RoomDB(name= name)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)

    return db_room

def get_room(db: Session, room_id: int):
    return db.query(RoomDB).filter(RoomDB.id == room_id).first()

