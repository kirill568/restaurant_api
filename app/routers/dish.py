from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from app.models.dish import Dish
from app.models.type_of_dish import Type_of_dish

from app.schemas.dish.create_dish_schema import Create_dish_schema
from app.schemas.dish.dish_schema import Dish_schema
from app.schemas.dish.update_dish_schema import Update_dish_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message

from app.repository import crud

router = APIRouter(
    prefix="", 
    tags=["dish"]
)

@router.get("/dishes", response_model=Union[List[Dish_schema], None])
async def get_dishes(db: AsyncSession = Depends(get_db)):
    all_items: List[Dish] = await crud.get_all(Dish, db)
    return all_items

@router.get("/dish/{id}", response_model=Dish_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
async def get_dish(id: int, db: AsyncSession = Depends(get_db)):
    item = await crud.get_by_id(Dish, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Dish not found"})
    
    return item

@router.post("/dish", response_model=Entity_created)
async def create_dish(item: Create_dish_schema, db: AsyncSession = Depends(get_db)):
    dish_type: Type_of_dish = await crud.get_by_id(Type_of_dish, item.type_of_dish_id, db)
    if dish_type is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Dish type not found"})

    item = await crud.create(Dish, item, db)
    return JSONResponse(content={"id": item.id})

@router.put("/dish/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def update_dish(id: int, item: Update_dish_schema, db: AsyncSession = Depends(get_db)):
    dish_type: Type_of_dish = await crud.get_by_id(Type_of_dish, item.type_of_dish_id, db)
    if dish_type is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Dish type not found"})

    item: Dish = await crud.update(Dish, item, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Dish not found"})

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish successfully updated"})

@router.delete("/dish/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def remove_dish(id: int, db: AsyncSession = Depends(get_db)):
    item: Dish = await crud.get_by_id(Dish, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Dish not found"})
    
    await crud.delete(Dish, id, db)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Dish successfully removed"})