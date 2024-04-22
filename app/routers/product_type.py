from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from app.models.type_of_product import Type_of_product

from app.schemas.product_type.create_product_type_schema import Create_product_type_schema
from app.schemas.product_type.product_type_schema import Product_type_schema
from app.schemas.product_type.update_product_type_schema import Update_product_type_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message

from app.repository import crud

router = APIRouter(
    prefix="/product-type", 
    tags=["product-type"]
)

@router.get("", response_model=Union[List[Product_type_schema], None])
async def get_product_types(db: AsyncSession = Depends(get_db)):
    all_items: List[Type_of_product] = await crud.get_all(Type_of_product, db)
    return all_items

@router.get("/{id}", response_model=Product_type_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
async def get_product_type(id: int, db: AsyncSession = Depends(get_db)):
    item: Type_of_product = await crud.get_by_id(Type_of_product, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product type not found"})
    
    return item

@router.post("", response_model=Entity_created)
async def create_product_type(item: Create_product_type_schema, db: AsyncSession = Depends(get_db)):
    item: Type_of_product = await crud.create(Type_of_product, item, db)
    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def update_product_type(id: int, item: Update_product_type_schema, db: AsyncSession = Depends(get_db)):
    item: Type_of_product = await crud.update(Type_of_product, item, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product type not found"})

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Product type successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def remove_product_type(id: int, db: AsyncSession = Depends(get_db)):
    item: Type_of_product = await crud.get_by_id(Type_of_product, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product type not found"})
    
    await crud.delete(Type_of_product, id, db)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Product type successfully removed"})