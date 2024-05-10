from sqlalchemy.ext.asyncio import AsyncSession
from app.models.bill import Bill
from sqlalchemy.future import select

async def create_bill(order_id: int, dish_id: int, db: AsyncSession):
    bill = Bill()
    bill.order_id = order_id
    bill.dish_id = dish_id

    db.add(bill)
    await db.commit()
    await db.refresh(bill)
    return bill

async def get_bills_for_order(order_id: int, db: AsyncSession):
    stmt = select(Bill).where(Bill.order_id == order_id)
    result = await db.execute(stmt)
    return result.scalars().all()