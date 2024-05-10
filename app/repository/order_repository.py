from sqlalchemy.ext.asyncio import AsyncSession
from app.models.order import Order
from datetime import datetime

async def create_order(client_id: int, timestamp: int, db: AsyncSession):
    order = Order()
    order.client_id = client_id
    order.date = datetime.fromtimestamp(timestamp)

    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order