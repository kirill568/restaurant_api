from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from app.database import get_db
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

from app.repository import crud
from app.repository.composition_of_dish import get_recipe_for_dish, delete_recipe_of_dish

router = APIRouter(
    prefix="/recipe", 
    tags=["recipe"]
)

# Help funtions
# -------------
async def is_dish_exist(id: int, db: AsyncSession):
    dish: Dish = await crud.get_by_id(Dish, id, db)
    if dish == None:
        return False, "Dish not found"
    
    return True, ""

async def is_product_exist(id: int, db: AsyncSession):
    product: Product = await crud.get_by_id(Product, id, db)
    if product == None:
        return False, "Product not found"
    
    return True, ""

async def is_unit_of_measurement_exist(id: int, db: AsyncSession):
    unit_of_measurement: Unit_of_measurement = await crud.get_by_id(Unit_of_measurement, id, db)
    if unit_of_measurement == None:
        return False, "Unit of measurement not found"
    
    return True, ""
# -------------

@router.get("/{dish_id}", response_model=List[Composition_of_dish_schema], responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
async def get_recipe_by_dish(dish_id: int, db: AsyncSession = Depends(get_db)):
    result, msg = await is_dish_exist(dish_id, db)
    if not result:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": msg})
    
    return await get_recipe_for_dish(dish_id, db)

@router.post("/{dish_id}", response_model=Entity_created)
async def create_recipe(dish_id: int, items: List[Create_composition_of_dish_schema], db: AsyncSession = Depends(get_db)):
    print(await is_dish_exist(dish_id, db))
    result, msg = await is_dish_exist(dish_id, db)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": msg})

    for item in items:
        result, msg = await is_product_exist(item.product_id, db)
        result, msg = await is_unit_of_measurement_exist(item.unit_of_measurement_id, db)
        if not result:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": msg})

    for item in items:
        item.dish_id = dish_id
        await crud.create(Composition_of_dish, item, db)

    return JSONResponse(content={"message": "Recipe successfully created"})

@router.put("/{dish_id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def update_recipe(dish_id: int, items: List[Update_composition_of_dish_schema], db: AsyncSession = Depends(get_db)):    
    result, msg = await is_dish_exist(dish_id, db)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": msg})

    for item in items:
        result, msg = await is_product_exist(item.product_id, db)
        result, msg = await is_unit_of_measurement_exist(item.unit_of_measurement_id, db)
        if not result:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": msg})
        
    await delete_recipe_of_dish(dish_id, db)

    for item in items:
        item.dish_id = dish_id
        await crud.create(Composition_of_dish, item, db)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Recipe successfully updated"})

@router.delete("/{dish_id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def remove_recipe_by_dish(dish_id: int, db: AsyncSession = Depends(get_db)):
    result, msg = await is_dish_exist(dish_id, db)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": msg})
    
    print(dish_id)
    await delete_recipe_of_dish(dish_id, db)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Recipe for dish successfully removed"})