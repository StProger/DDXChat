from fastapi import APIRouter


router = APIRouter(prefix="/chats",
                   tags=["Чаты"])


@router.get("/history")
async def get_history(
        first_user_id: int,
        second_user_id: int
):

    ...

