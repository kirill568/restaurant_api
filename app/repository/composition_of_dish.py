from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from app.models.composition_of_dish import Composition_of_dish

async def get_recipe_for_dish(dish_id: int, db: AsyncSession):
    stmt = select(Composition_of_dish).where(Composition_of_dish.dish_id == dish_id)
    result = await db.execute(stmt)
    return result.scalars().all()

async def delete_recipe_of_dish(dish_id: int, db: AsyncSession):
    print(dish_id)
    stmt = delete(Composition_of_dish).where(Composition_of_dish.dish_id == dish_id)
    print(stmt)
    await db.execute(stmt)
    await db.commit()