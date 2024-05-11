from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.type_of_dish import Type_of_dish

from app.schemas.dish_type.create_dish_type_schema import Create_dish_type_schema
from app.schemas.dish_type.dish_type_schema import Dish_type_schema
from app.schemas.dish_type.update_dish_type_schema import Update_dish_type_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message

from app.repository import TypeOfDishRepository

from app.container import Container

from app.exceptions import NotFoundError

router = APIRouter(
    prefix="/dish-type", 
    tags=["dish-type"]
)

# dependencies
# -------------
@inject
async def valid_dish_type_id(id: int, repository: TypeOfDishRepository = Depends(Provide[Container.type_of_dish_repository])):
    dish_type: Type_of_dish = await repository.get_by_id(id)
    if dish_type == None:
        raise NotFoundError("Dish type not found")
    
    return dish_type
# -------------

@router.get("", response_model=Union[List[Dish_type_schema], None])
@inject
async def get_dish_types(repository: TypeOfDishRepository = Depends(Provide[Container.type_of_dish_repository])):
    return await repository.get_all()

@router.get("/{id}", response_model=Dish_type_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def get_dish_type(type_of_dish: Type_of_dish = Depends(valid_dish_type_id)):    
    return type_of_dish

@router.post("", response_model=Entity_created)
@inject
async def create_dish_type(item: Create_dish_type_schema, repository: TypeOfDishRepository = Depends(Provide[Container.type_of_dish_repository])):
    item: Type_of_dish = await repository.create(item)
    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_dish_type(
    item: Update_dish_type_schema, 
    type_of_dish: Type_of_dish = Depends(valid_dish_type_id), 
    repository: TypeOfDishRepository = Depends(Provide[Container.type_of_dish_repository])
):
    item: Type_of_dish = await repository.update(item, type_of_dish.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish type successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_dish_type(
    type_of_dish: Type_of_dish = Depends(valid_dish_type_id), 
    repository: TypeOfDishRepository = Depends(Provide[Container.type_of_dish_repository])
):    
    await repository.delete(type_of_dish.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish type successfully removed"})