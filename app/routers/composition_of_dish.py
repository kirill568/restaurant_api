from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from app.models.composition_of_dish import Composition_of_dish
from app.models.dish import Dish
from app.models.product import Product
from app.models.unit_of_measurement import Unit_of_measurement

from app.schemas.composition_of_dish.create_composition_of_dish_schema import Create_composition_of_dish_schema
from app.schemas.composition_of_dish.composition_of_dish_schema import Composition_of_dish_schema
from app.schemas.composition_of_dish.update_composition_of_dish_schema import Update_composition_of_dish_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message

from app.repository import CompositionOfDishRepository

from app.services import CompositionOfDishService

from app.container import Container

from app.exceptions import NotFoundError

router = APIRouter(
    prefix="/recipe", 
    tags=["recipe"]
)

# dependencies
# -------------
@inject
async def valid_dish_id(dish_id: int, repository: CompositionOfDishRepository = Depends(Provide[Container.composition_of_dish_repository])):
    dish: Dish = await repository.get_by_id(dish_id)
    if dish == None:
        raise NotFoundError("Recipe not found")
    
    return dish
# -------------

@router.get("/{dish_id}", response_model=List[Composition_of_dish_schema], responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def get_recipe_by_dish(dish: Dish = Depends(valid_dish_id), repository: CompositionOfDishRepository = Depends(Provide[Container.composition_of_dish_repository])):    
    return await repository.get_recipe_for_dish(dish.id)

@router.post("/{dish_id}", response_model=Entity_created)
@inject
async def create_recipe(
    items: List[Create_composition_of_dish_schema], 
    dish: Dish = Depends(valid_dish_id),
    service: CompositionOfDishService = Depends(Provide[Container.composition_of_dish_service])
):
    service.create_recipe(dish.id, items)

    return JSONResponse(content={"message": "Recipe successfully created"})

@router.put("/{dish_id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_recipe(
    items: List[Update_composition_of_dish_schema], 
    dish: Dish = Depends(valid_dish_id),
    service: CompositionOfDishService = Depends(Provide[Container.composition_of_dish_service])
):    
    service.update_recipe(dish.id, items)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Recipe successfully updated"})

@router.delete("/{dish_id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_recipe_by_dish(dish: Dish = Depends(valid_dish_id), repository: CompositionOfDishRepository = Depends(Provide[Container.composition_of_dish_repository])):
    await repository.delete_recipe_of_dish(dish.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Recipe for dish successfully removed"})