from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.base import BaseModel
from pydantic import BaseModel as BaseSchema

class BaseRepository:
    def __init__(self, session: AsyncSession, model: BaseModel) -> None:
        self.session = session
        self.model = model

    async def get_by_id(self, id: int):
        async with self.session() as session:
            return await session.get(self.model, id)

    async def get_all(self):
        async with self.session() as session:
            result = await session.execute(select(self.model))
            return result.scalars().all()

    async def create(self, schema: BaseSchema):
        async with self.session() as session:
            db_model = self.model(**schema.model_dump())
            session.add(db_model)
            await session.commit()
            await session.refresh(db_model)
            return db_model

    async def update(self, schema: BaseSchema, id):
        async with self.session() as session:
            db_model = await session.get(self.model, id)
            if db_model is None:
                return None
            
            for var, value in vars(schema).items():
                setattr(db_model, var, value) if value else None

            await session.commit()
            await session.refresh(db_model)
            return await self.get_by_id(id)

    async def delete(self, id: int):
        async with self.session() as session:
            db_user = await self.get_by_id(id)
            if db_user is None:
                return
            
            await session.delete(db_user)
            await session.commit()