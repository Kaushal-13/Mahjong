from fastapi import APIRouter

import sys
sys.path.append("..")
from services.room_service import create_new_room

rooms_router = APIRouter()

@rooms_router.post("/rooms")
def create_room_handler():
    return create_new_room()