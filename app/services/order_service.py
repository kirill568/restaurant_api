from app.services.base_service import BaseService

from app.models.client import Client
from app.models.dish import Dish
from app.models.order import Order
from app.models.bill import Bill

from app.repository.order_repository import OrderRepository
from app.repository.bill_repository import BillRepository
from app.repository.client_repository import ClientRepository
from app.repository.dish_repository import DishRepository

from app.schemas.bill.create_bill_schema import Create_bill_schema
from app.schemas.order.create_orm_entity_order_schema import Create_orm_entity_order_schema
from app.schemas.order.create_order_schema import Create_order_schema
from app.schemas.order.order_schema import Order_schema

from app.exceptions import NotFoundError

from datetime import datetime

from typing import List

class OrderService(BaseService):
    def __init__(self, order_repository: OrderRepository, bill_repository: BillRepository, client_repository: ClientRepository, dish_repository: DishRepository):
        self.order_repository = order_repository
        self.bill_repository = bill_repository
        self.client_repository = client_repository
        self.dish_repository = dish_repository
        super().__init__(order_repository)

    async def create_order(self, item: Create_order_schema):
        self._is_client_exist(item.client_id)

        order_schema = Create_orm_entity_order_schema(
            client_id = item.client_id,
            date = datetime.fromtimestamp(item.timestamp)
        )
        order: Order = await self.order_repository.create(order_schema)

        order_price: float = 0.0
        for dish_id in item.dishes_ids:
            dish: Dish = await self.dish_repository.get_by_id(dish_id)
            if dish is None:
                await self.order_repository.delete(order.id)
                raise NotFoundError(f"Dish with id {dish_id} not found")

            bill_schema = Create_bill_schema(
                order_id = order.id,
                dish_id = dish.id
            )
            await self.bill_repository.create(bill_schema)

            order_price += dish.cost

        return order.id, order_price
    
    async def get_all_orders(self):
        all_orders: List[Order] = await self.order_repository.get_all()

        result = []
        for order in all_orders:
            result_item = await self.prepare_order(order)

            result.append(result_item)

        return result
    
    async def prepare_order(self, order: Order):
        bills: List[Bill] = await self.bill_repository.get_bills_for_order(order.id)

        return Order_schema(
            id=order.id,
            client_id=order.client_id, 
            timestamp=datetime.timestamp(order.date),
            dishes_ids=map(lambda bill: bill.dish_id, bills)
        )

    async def _is_client_exist(self, client_id: int):
        client: Client = await self.client_repository.get_by_id(client_id)
        if client == None:
            return NotFoundError("Client not found")
        
        return True