from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.type_of_dish import TypeOfDish

from app.schemas.dish_type.create_dish_type_schema import CreateDishTypeSchema
from app.schemas.dish_type.dish_type_schema import DishTypeSchema
from app.schemas.dish_type.update_dish_type_schema import UpdateDishTypeSchema

from app.schemas.responses.entity_created import EntityCreated
from app.schemas.responses.message import Message

from app.repository import TypeOfDishRepository

from app.container import Container

from app.dependencies.dish_type_dependencies import valid_dish_type_id

router = APIRouter(
    prefix="/dish-type", 
    tags=["dish-type"]
)

@router.get("", response_model=Union[List[DishTypeSchema], None])
@inject
async def get_dish_types(repository: TypeOfDishRepository = Depends(Provide[Container.type_of_dish_repository])):
    return await repository.get_all()

@router.get("/{id}", response_model=DishTypeSchema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def get_dish_type(type_of_dish: TypeOfDish = Depends(valid_dish_type_id)):    
    return type_of_dish

@router.post("", response_model=EntityCreated)
@inject
async def create_dish_type(item: CreateDishTypeSchema, repository: TypeOfDishRepository = Depends(Provide[Container.type_of_dish_repository])):
    item: TypeOfDish = await repository.create(item)
    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_dish_type(
    item: UpdateDishTypeSchema, 
    type_of_dish: TypeOfDish = Depends(valid_dish_type_id), 
    repository: TypeOfDishRepository = Depends(Provide[Container.type_of_dish_repository])
):
    item: TypeOfDish = await repository.update(item, type_of_dish.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish type successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_dish_type(
    type_of_dish: TypeOfDish = Depends(valid_dish_type_id), 
    repository: TypeOfDishRepository = Depends(Provide[Container.type_of_dish_repository])
):    
    await repository.delete(type_of_dish.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish type successfully removed"})