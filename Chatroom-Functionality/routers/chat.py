from fastapi import WebSocket, APIRouter

import sys
sys.path.append("..")
from services.chat_service import handle_chat

chat_router = APIRouter()

@chat_router.websocket("/rooms/{room_id}/messages/{username}")
async def websocket_endpoint(room_id: int, username: str, websocket: WebSocket):
    await handle_chat(room_id, username, websocket)