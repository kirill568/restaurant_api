from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from app.models.composition_of_dish import CompositionOfDish
from app.repository.base_repository import BaseRepository

class CompositionOfDishRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, CompositionOfDish)

    async def get_recipe_for_dish(self, dish_id: int):
        async with self.session() as session:
            stmt = select(CompositionOfDish).where(CompositionOfDish.dish_id == dish_id)
            result = await session.execute(stmt)
            return result.scalars().all()

    async def delete_recipe_of_dish(self, dish_id: int):
        async with self.session() as session:
            stmt = delete(CompositionOfDish).where(CompositionOfDish.dish_id == dish_id)
            await session.execute(stmt)
            await session.commit()