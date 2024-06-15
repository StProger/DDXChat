import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.messages import manager


router = APIRouter(prefix="/fitness_messages", tags=["Сообщения"])


@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            data_json = json.loads(data)
            await manager.send_personal_message(data_json, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
