from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.dish import Dish

from app.schemas.composition_of_dish.create_composition_of_dish_schema import CreateCompositionOfDishSchema
from app.schemas.composition_of_dish.composition_of_dish_schema import CompositionOfDishSchema
from app.schemas.composition_of_dish.update_composition_of_dish_schema import UpdateCompositionOfDishSchema

from app.schemas.responses.entity_created import EntityCreated
from app.schemas.responses.message import Message

from app.repository import CompositionOfDishRepository

from app.services import CompositionOfDishService

from app.container import Container

from app.dependencies.dish_dependencies import valid_dish_id

router = APIRouter(
    prefix="/recipe", 
    tags=["recipe"]
)

@router.get("/{dish_id}", response_model=List[CompositionOfDishSchema], responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def get_recipe_by_dish(dish: Dish = Depends(valid_dish_id), repository: CompositionOfDishRepository = Depends(Provide[Container.composition_of_dish_repository])):    
    return await repository.get_recipe_for_dish(dish.id)

@router.post("/{dish_id}", response_model=EntityCreated)
@inject
async def create_recipe(
    items: List[CreateCompositionOfDishSchema], 
    dish: Dish = Depends(valid_dish_id),
    service: CompositionOfDishService = Depends(Provide[Container.composition_of_dish_service])
):
    await service.create_recipe(dish.id, items)

    return JSONResponse(content={"message": "Recipe successfully created"})

@router.put("/{dish_id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_recipe(
    items: List[UpdateCompositionOfDishSchema], 
    dish: Dish = Depends(valid_dish_id),
    service: CompositionOfDishService = Depends(Provide[Container.composition_of_dish_service])
):    
    await service.update_recipe(dish.id, items)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Recipe successfully updated"})

@router.delete("/{dish_id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_recipe_by_dish(dish: Dish = Depends(valid_dish_id), repository: CompositionOfDishRepository = Depends(Provide[Container.composition_of_dish_repository])):
    await repository.delete_recipe_of_dish(dish.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Recipe for dish successfully removed"})