from fastapi import APIRouter, Query

from app.chats.dao import ChatsDAO
from app.messages.dao import MessagesDAO
from app.messages.schemas import SMessages
from app.chats.utils import choose_dialogs_user


router = APIRouter(prefix="/chats",
                   tags=["Чаты"])


@router.get("/{user_id}/dialogs", description="Получение списка диалогов пользователя.")
async def get_dialogs(
        user_id: int
) -> list[int]:

    dialogs = await ChatsDAO.get_user_dialogs(user_id=user_id)

    if not dialogs:
        return []
    else:

        return choose_dialogs_user(user_id=user_id, dialogs=dialogs)


@router.get("/history", description="Получение истории сообщений между двумя пользователями.")
async def get_history(
        first_user_id: int = Query(
            default=...,
            description="Идентификатор первого пользователя, для которого нужно найти истории сообщений."
        ),
        second_user_id: int = Query(
            default=...,
            description="Идентификатор второго пользователя, для которого нужно найти истории сообщений."
        )
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


@router.post("", description="Создание чата с юзером.")
async def create_chat(
        first_user_id: int = Query(
            default=...,
            description="Идентификатор первого пользователя, для которого нужно создать чат."
        ),
        second_user_id: int = Query(
            default=...,
            description="Идентификатор второго пользователя, для которого нужно создать чат."
        )
) -> list[SMessages]:

    chat = await ChatsDAO.get_chat(first_user_id=first_user_id, second_user_id=second_user_id)

    if chat is None:

        await ChatsDAO.add(first_user_id=first_user_id, second_user_id=second_user_id)
        return []
    else:
        chat = await ChatsDAO.find_by_id(model_id=chat.id)
        messages = await MessagesDAO.find_all(chat_id=chat.id)
        return messages


@router.delete("", description="Удаление чата с юзером.")
async def delete_dialog(
        first_user_id: int = Query(
            default=...,
            description="Идентификатор первого пользователя, для которого нужно удалить чат."
        ),
        second_user_id: int = Query(
            default=...,
            description="Идентификатор второго пользователя, для которого нужно удалить чат."
        )
) -> None:

    await ChatsDAO.delete_dialog(
        first_user_id=first_user_id,
        second_user_id=second_user_id
    )