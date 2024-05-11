from sqlalchemy.ext.asyncio import AsyncSession
from app.models.dish import Dish
from app.repository.base_repository import BaseRepository

class DishRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, Dish)