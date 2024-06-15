from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.database import engine, Base

from app.messages.models import Messages
from app.chats.models import Chats

from app.chats.router import router as chat_router
from app.messages.router import router as message_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan, docs_url="/chat/docs")

app.include_router(chat_router)
app.include_router(message_router)