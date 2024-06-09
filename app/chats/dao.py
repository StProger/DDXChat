from sqlalchemy import select, or_, and_, Result

from app.chats.models import Chats
from app.dao.bases import BaseDAO

from app.database import async_session_maker


class ChatsDAO(BaseDAO):

    model = Chats

    @classmethod
    async def get_chat(
            cls,
            first_user_id: int,
            second_user_id: int
    ):

        async with async_session_maker() as session:

            query = select(Chats.__table__.columns).where(
                or_(
                    and_(
                        Chats.first_user_id == first_user_id,
                        Chats.second_user_id == second_user_id
                    ),
                    and_(
                        Chats.first_user_id == second_user_id,
                        Chats.second_user_id == first_user_id
                    )
                )
            )

            result: Result = await session.execute(query)

            return result.one_or_none()

