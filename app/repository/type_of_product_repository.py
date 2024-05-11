from sqlalchemy.ext.asyncio import AsyncSession
from app.models.type_of_product import TypeOfProduct
from app.repository.base_repository import BaseRepository

class TypeOfProductRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, TypeOfProduct)