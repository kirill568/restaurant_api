from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.dish import Dish

from app.schemas.dish.create_dish_schema import Create_dish_schema
from app.schemas.dish.dish_schema import Dish_schema
from app.schemas.dish.update_dish_schema import Update_dish_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message

from app.services import DishService

from app.repository import DishRepository

from app.container import Container

from app.exceptions import NotFoundError

router = APIRouter(
    prefix="", 
    tags=["dish"]
)

# dependencies
# -------------
@inject
async def valid_dish_id(id: int, repository: DishRepository = Depends(Provide[Container.dish_repository])):
    dish: Dish = await repository.get_by_id(id)
    if dish == None:
        raise NotFoundError("Dish not found")
    
    return dish
# -------------

@router.get("/dishes", response_model=Union[List[Dish_schema], None])
@inject
async def get_dishes(repository: DishRepository = Depends(Provide[Container.dish_repository])):
    return await repository.get_all()

@router.get("/dish/{id}", response_model=Dish_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def get_dish(dish: Dish = Depends(valid_dish_id)):    
    return dish

@router.post("/dish", response_model=Entity_created)
@inject
async def create_dish(item: Create_dish_schema, service: DishService = Depends(Provide[Container.dish_service])):
    item = await service.create_dish(item)

    return JSONResponse(content={"id": item.id})

@router.put("/dish/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_dish(item: Update_dish_schema, dish: Dish = Depends(valid_dish_id), service: DishService = Depends(Provide[Container.dish_service])):    
    item = await service.update_dish(item, dish.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish successfully updated"})

@router.delete("/dish/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_dish(dish: Dish = Depends(valid_dish_id), repository: DishRepository = Depends(Provide[Container.dish_repository])):    
    await repository.delete(dish.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish successfully removed"})