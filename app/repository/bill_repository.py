from sqlalchemy.ext.asyncio import AsyncSession
from app.models.bill import Bill
from sqlalchemy.future import select
from app.repository.base_repository import BaseRepository

class BillRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, Bill)

    async def get_bills_for_order(self, order_id: int):
        async with self.session() as session:
            stmt = select(Bill).where(Bill.order_id == order_id)
            result = await session.execute(stmt)
            return result.scalars().all()