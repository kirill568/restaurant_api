from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.dish import Dish

from app.schemas.dish.create_dish_schema import CreateDishSchema
from app.schemas.dish.dish_schema import DishSchema
from app.schemas.dish.update_dish_schema import UpdateDishSchema

from app.schemas.responses.entity_created import EntityCreated
from app.schemas.responses.message import Message

from app.services import DishService

from app.repository import DishRepository

from app.container import Container

from app.dependencies.dish_dependencies import valid_dish_id

router = APIRouter(
    prefix="", 
    tags=["dish"]
)

@router.get("/dishes", response_model=Union[List[DishSchema], None])
@inject
async def get_dishes(repository: DishRepository = Depends(Provide[Container.dish_repository])):
    return await repository.get_all()

@router.get("/dish/{id}", response_model=DishSchema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def get_dish(dish: Dish = Depends(valid_dish_id)):    
    return dish

@router.post("/dish", response_model=EntityCreated)
@inject
async def create_dish(item: CreateDishSchema, service: DishService = Depends(Provide[Container.dish_service])):
    item = await service.create_dish(item)

    return JSONResponse(content={"id": item.id})

@router.put("/dish/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_dish(item: UpdateDishSchema, dish: Dish = Depends(valid_dish_id), service: DishService = Depends(Provide[Container.dish_service])):    
    item = await service.update_dish(item, dish.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish successfully updated"})

@router.delete("/dish/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_dish(dish: Dish = Depends(valid_dish_id), repository: DishRepository = Depends(Provide[Container.dish_repository])):    
    await repository.delete(dish.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish successfully removed"})