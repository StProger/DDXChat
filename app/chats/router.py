from fastapi import APIRouter

from app.chats.dao import ChatsDAO
from app.messages.dao import MessagesDAO
from app.messages.schemas import SMessages
from app.chats.utils import choose_dialogs_user


router = APIRouter(prefix="/chats",
                   tags=["Чаты"])


@router.get("/{user_id}/dialogs")
async def get_dialogs(
        user_id: int
):

    dialogs = await ChatsDAO.get_user_dialogs(user_id=user_id)

    if not dialogs:
        return []
    else:

        return choose_dialogs_user(user_id=user_id, dialogs=dialogs)


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


@router.post("")
async def create_chat(
        first_user_id: int,
        second_user_id: int
) -> list[SMessages]:

    chat = await ChatsDAO.get_chat(first_user_id=first_user_id, second_user_id=second_user_id)

    if chat is None:

        await ChatsDAO.add(first_user_id=first_user_id, second_user_id=second_user_id)
        return []
    else:
        chat = await ChatsDAO.find_by_id(model_id=chat.id)
        messages = await MessagesDAO.find_all(chat_id=chat.id)
        return messages


@router.delete("")
async def delete_dialog(
        first_user_id: int,
        second_user_id: int
):

    await ChatsDAO.delete_dialog(
        first_user_id=first_user_id,
        second_user_id=second_user_id
    )