from fastapi import APIRouter

from app.chats.dao import ChatsDAO
from app.messages.dao import MessagesDAO
from app.messages.schemas import SMessages


router = APIRouter(prefix="/chats",
                   tags=["Чаты"])


@router.get("/history")
async def get_history(
        first_user_id: int,
        second_user_id: int
) -> list[SMessages]:

    chat = await ChatsDAO.get_chat(
        first_user_id=first_user_id,
        second_user_id=second_user_id
    )
    if chat is None:

        await ChatsDAO.add(first_user_id=first_user_id, second_user_id=second_user_id)
        return []
    else:
        chat = await ChatsDAO.find_by_id(model_id=chat.id)
        messages = await MessagesDAO.find_all(chat_id=chat.id)
        return messages

