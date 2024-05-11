from sqlalchemy.ext.asyncio import AsyncSession
from app.models.client import Client
from app.repository.base_repository import BaseRepository

class ClientRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, Client)