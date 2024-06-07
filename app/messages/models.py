from app.database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from datetime import datetime


class Messages(Base):

    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    sender_id: Mapped[int]
    receiver_id: Mapped[int]
    message_text: Mapped[str]
    timestamp: Mapped[datetime] = mapped_column()
