from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from datetime import datetime

from app.models.order import Order
from app.models.bill import Bill
from app.models.dish import Dish
from app.models.client import Client

from app.schemas.order.create_order_schema import Create_order_schema
from app.schemas.order.order_schema import Order_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message

from app.repository import bill_repository, crud, order_repository

router = APIRouter(
    prefix="/order", 
    tags=["order"]
)

@router.post("", response_model=Entity_created)
async def create_order(item: Create_order_schema, db: AsyncSession = Depends(get_db)):
    client: Client = await crud.get_by_id(Client, item.client_id, db)
    if client == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Client not found"})

    order = await order_repository.create_order(item.client_id, item.timestamp, db)

    order_price: float = 0.0
    for dish_id in item.dishes_ids:
        dish: Dish = await crud.get_by_id(Dish, dish_id, db)
        if dish is None:
            await crud.delete(Order, order.id, db)
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": f"Dish with id {dish_id} not found"})

        await bill_repository.create_bill(order.id, dish.id, db)

        order_price += dish.cost

    return JSONResponse(content={"id": order.id, "order_price": order_price})

@router.get("", response_model=Union[List[Order_schema], None])
async def get_orders(db: AsyncSession = Depends(get_db)):
    all_orders: List[Order] = await crud.get_all(Order, db)

    result = []
    for order in all_orders:
        result_item = {}
        result_item["id"] = order.id
        result_item["client_id"] = order.client_id
        result_item["timestamp"] = datetime.timestamp(order.date)

        bills: List[Bill] = await bill_repository.get_bills_for_order(order.id, db)
        
        result_item["dishes_ids"] = map(lambda bill: bill.dish_id, bills)

        result.append(result_item)

    return result

@router.get("/{id}", response_model=Order_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
async def get_order(id: int, db: AsyncSession = Depends(get_db)):
    order = await crud.get_by_id(Order, id, db)
    if order == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product not found"})
    
    result = {}
    result["id"] = order.id
    result["client_id"] = order.client_id
    result["timestamp"] = datetime.timestamp(order.date)

    bills: List[Bill] = await bill_repository.get_bills_for_order(order.id, db)
    
    result["dishes_ids"] = map(lambda bill: bill.dish_id, bills)

    return result