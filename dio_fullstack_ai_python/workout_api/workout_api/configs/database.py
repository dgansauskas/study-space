from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from workout_api.configs.settings import settings


engine = create_async_engine(settings.DB_URL, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession) 

async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()