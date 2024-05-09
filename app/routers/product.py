from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from app.models.product import Product
from app.models.type_of_product import Type_of_product

from app.schemas.product.create_product_schema import Create_product_schema
from app.schemas.product.product_schema import Product_schema
from app.schemas.product.update_product_schema import Update_product_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message

from app.repository import crud

router = APIRouter(
    prefix="/product", 
    tags=["product"]
)

@router.get("", response_model=Union[List[Product_schema], None])
async def get_products(db: AsyncSession = Depends(get_db)):
    all_items: List[Product] = await crud.get_all(Product, db)
    return all_items

@router.get("/{id}", response_model=Product_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
async def get_product(id: int, db: AsyncSession = Depends(get_db)):
    item = await crud.get_by_id(Product, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product not found"})
    
    return item

@router.post("", response_model=Entity_created)
async def create_product(item: Create_product_schema, db: AsyncSession = Depends(get_db)):
    product_type: Type_of_product = await crud.get_by_id(Type_of_product, item.type_of_product_id, db)
    if product_type is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product type not found"})

    item = await crud.create(Product, item, db)
    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def update_product(id: int, item: Update_product_schema, db: AsyncSession = Depends(get_db)):
    product_type: Type_of_product = await crud.get_by_id(Type_of_product, item.type_of_product_id, db)
    if product_type is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product type not found"})

    item: Product = await crud.update(Product, item, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product not found"})

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Product successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def remove_product_type(id: int, db: AsyncSession = Depends(get_db)):
    item: Product = await crud.get_by_id(Product, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product not found"})
    
    await crud.delete(Product, id, db)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Product successfully removed"})