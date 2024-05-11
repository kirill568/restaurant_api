from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from app.repository.base_repository import BaseRepository

class ProductRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, Product)