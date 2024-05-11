from sqlalchemy.ext.asyncio import AsyncSession
from app.models.unit_of_measurement import Unit_of_measurement
from app.repository.base_repository import BaseRepository

class UnitOfMeasurementRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, Unit_of_measurement)