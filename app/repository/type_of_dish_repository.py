from sqlalchemy.ext.asyncio import AsyncSession
from app.models.type_of_dish import TypeOfDish
from app.repository.base_repository import BaseRepository

class TypeOfDishRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, TypeOfDish)