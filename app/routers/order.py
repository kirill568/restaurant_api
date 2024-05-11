from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.order import Order

from app.schemas.order.create_order_schema import CreateOrderSchema
from app.schemas.order.order_schema import OrderSchema

from app.schemas.responses.entity_created import EntityCreated
from app.schemas.responses.message import Message

from app.repository import OrderRepository
from app.services import OrderService

from app.container import Container

from app.exceptions import NotFoundError

router = APIRouter(
    prefix="/order", 
    tags=["order"]
)

# dependencies
# -------------
@inject
async def valid_order_id(id: int, repository: OrderRepository = Depends(Provide[Container.order_repository])):
    order: Order = await repository.get_by_id(id)
    if order == None:
        raise NotFoundError("Order not found")
    
    return order
# -------------

@router.post("", response_model=EntityCreated)
@inject
async def create_order(item: CreateOrderSchema, service: OrderService = Depends(Provide[Container.order_service])):
    order_id, order_price = await service.create_order(item)

    return JSONResponse(content={"id": order_id, "order_price": order_price})

@router.get("", response_model=Union[List[OrderSchema], None])
@inject
async def get_orders(
    repository: OrderRepository = Depends(Provide[Container.order_repository]), 
    service: OrderService = Depends(Provide[Container.order_service])
):
    all_orders: List[Order] = await repository.get_all()

    result = []
    for order in all_orders:
        result_item = await service.prepare_order(order)

        result.append(result_item)

    return result

@router.get("/{id}", response_model=OrderSchema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def get_order(order: Order = Depends(valid_order_id), service: OrderService = Depends(Provide[Container.order_service])):
    return await service.prepare_order(order)