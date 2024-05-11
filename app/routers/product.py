from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.product import Product
from app.models.type_of_product import TypeOfProduct

from app.schemas.product.create_product_schema import CreateProductSchema
from app.schemas.product.product_schema import ProductSchema
from app.schemas.product.update_product_schema import UpdateProductSchema

from app.schemas.responses.entity_created import EntityCreated
from app.schemas.responses.message import Message

from app.services import ProductService

from app.repository import ProductRepository

from app.container import Container

from app.exceptions import NotFoundError

router = APIRouter(
    prefix="/product", 
    tags=["product"]
)

# dependencies
# -------------
@inject
async def valid_product_id(id: int, repository: ProductRepository = Depends(Provide[Container.product_repository])):
    product: Product = await repository.get_by_id(id)
    if product == None:
        raise NotFoundError("Product not found")
    
    return product
# -------------

@router.get("", response_model=Union[List[ProductSchema], None])
@inject
async def get_products(repository: ProductRepository = Depends(Provide[Container.product_repository])):
    return await repository.get_all()

@router.get("/{id}", response_model=ProductSchema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def get_product(product: Product = Depends(valid_product_id)):    
    return product

@router.post("", response_model=EntityCreated)
@inject
async def create_product(
    item: CreateProductSchema, 
    service: ProductService = Depends(Provide[Container.product_service])
):
    item = await service.create_product(item)

    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_product(
    item: CreateProductSchema, 
    product: Product = Depends(valid_product_id),
    service: ProductService = Depends(Provide[Container.product_service])
):
    await service.update_product(item, product.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Product successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_product_type(product: Product = Depends(valid_product_id), repository: ProductRepository = Depends(Provide[Container.product_repository])):    
    await repository.delete(product.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Product successfully removed"})