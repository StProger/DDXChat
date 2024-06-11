from fastapi import WebSocket

import datetime

from app.messages.dao import MessagesDAO
from app.chats.dao import ChatsDAO


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, data: dict, websocket: WebSocket):

        dt = datetime.datetime.utcnow()
        data["dt"] = dt

        await self.add_message_to_db(data)

        await websocket.send_json(
            {
                "sender_id": data["sender_id"],
                "receiver_id": data["receiver_id"],
                "timestamp": str(dt),
                "message": data.get("message_text"),
                "training_id": data.get("training_id"),
                "exercise_id": data.get("exercise_id"),
                "nutrition_id": data.get("nutrition_id")
            }
        )

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    @staticmethod
    async def add_message_to_db(data):

        dt = data["dt"]
        sender_id = data['sender_id']
        receiver_id = data['receiver_id']
        chat = await ChatsDAO.get_chat(first_user_id=sender_id, second_user_id=receiver_id)
        message_text = data.get('message_text')
        training_id = data.get("training_id")
        exercise_id = data.get("exercise_id")
        nutrition_id = data.get("nutrition_id")


        await MessagesDAO.add(
            chat_id=chat.id,
            sender_id=sender_id,
            receiver_id=receiver_id,
            message_text=message_text,
            training_id=training_id,
            exercise_id=exercise_id,
            nutrition_id=nutrition_id,
            timestamp=dt
        )

