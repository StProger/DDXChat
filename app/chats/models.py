from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Chats(Base):

    __tablename__ = 'chats'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_user_id: Mapped[int] = mapped_column(nullable=False)
    second_user_id: Mapped[int] = mapped_column(nullable=False)
