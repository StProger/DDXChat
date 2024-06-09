from datetime import datetime

from pydantic import BaseModel


class SMessages(BaseModel):

    id: int
    chat_id: int
    sender_id: int
    receiver_id: int
    message_text: str
    timestamp: datetime