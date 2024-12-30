import json
from fastapi import WebSocket

import sys
sys.path.append("..")
from db.database import SessionLocal

import sys
sys.path.append("..")
from dao.room_dao import get_room

from typing import Dict, List

active_connections: Dict[int, List[WebSocket]] = {}

async def handle_chat(room_id: int, username: str, websocket: WebSocket):
    await websocket.accept()

    db = SessionLocal()
    room = get_room(db, room_id)
    db.close()

    if not room:
        await websocket.close()
        return
    
    if room_id not in active_connections:
        active_connections[room_id] = []
    
    active_connections[room_id].append(websocket)

    join_message = json.dumps({"user_id": "", "message": f"{username} has joined the chat."})
    for connection in active_connections[room_id]:
        if connection != websocket:
            await connection.send_text(join_message)

    try:
        while True:
            message = await websocket.receive_text()
            message_data = {
                            "user_id": username,
                            "message": message,
                            }
            message_json = json.dumps(message_data)

            for connection in active_connections[room_id]:
                    await connection.send_text(message_json)

    except:
         pass
    
    finally:
        active_connections[room_id].remove(websocket)
        leave_message = json.dumps({"user_id": "", "message": f"{username} has left the chat."})
        for connection in active_connections[room_id]:
             await connection.send_text(leave_message)
