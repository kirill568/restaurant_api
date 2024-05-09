from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from app.models.type_of_dish import Type_of_dish

from app.schemas.dish_type.create_dish_type_schema import Create_dish_type_schema
from app.schemas.dish_type.dish_type_schema import Dish_type_schema
from app.schemas.dish_type.update_dish_type_schema import Update_dish_type_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message

from app.repository import crud

router = APIRouter(
    prefix="/dish-type", 
    tags=["dish-type"]
)

@router.get("", response_model=Union[List[Dish_type_schema], None])
async def get_dish_types(db: AsyncSession = Depends(get_db)):
    all_items: List[Type_of_dish] = await crud.get_all(Type_of_dish, db)
    return all_items

@router.get("/{id}", response_model=Dish_type_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
async def get_dish_type(id: int, db: AsyncSession = Depends(get_db)):
    item: Type_of_dish = await crud.get_by_id(Type_of_dish, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Dish type not found"})
    
    return item

@router.post("", response_model=Entity_created)
async def create_dish_type(item: Create_dish_type_schema, db: AsyncSession = Depends(get_db)):
    item: Type_of_dish = await crud.create(Type_of_dish, item, db)
    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def update_dish_type(id: int, item: Update_dish_type_schema, db: AsyncSession = Depends(get_db)):
    item: Type_of_dish = await crud.update(Type_of_dish, item, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Dish type not found"})

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish type successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def remove_dish_type(id: int, db: AsyncSession = Depends(get_db)):
    item: Type_of_dish = await crud.get_by_id(Type_of_dish, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Dish type not found"})
    
    await crud.delete(Type_of_dish, id, db)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish type successfully removed"})