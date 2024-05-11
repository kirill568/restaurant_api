from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.type_of_product import Type_of_product

from app.schemas.product_type.create_product_type_schema import Create_product_type_schema
from app.schemas.product_type.product_type_schema import Product_type_schema
from app.schemas.product_type.update_product_type_schema import Update_product_type_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message


from app.repository import TypeOfProductRepository

from app.container import Container

from app.exceptions import NotFoundError

router = APIRouter(
    prefix="/product-type", 
    tags=["product-type"]
)

# dependencies
# -------------
@inject
async def valid_product_type_id(id: int, repository: TypeOfProductRepository = Depends(Provide[Container.type_of_product_repository])):
    product_type: Type_of_product = await repository.get_by_id(id)
    if product_type == None:
        raise NotFoundError("Product type not found")
    
    return product_type
# -------------

@router.get("", response_model=Union[List[Product_type_schema], None])
@inject
async def get_product_types(repository: TypeOfProductRepository = Depends(Provide[Container.type_of_product_repository])):
    return await repository.get_all()

@router.get("/{id}", response_model=Product_type_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def get_product_type(product_type: Type_of_product = Depends(valid_product_type_id)):    
    return product_type

@router.post("", response_model=Entity_created)
@inject
async def create_product_type(item: Create_product_type_schema, repository: TypeOfProductRepository = Depends(Provide[Container.type_of_product_repository])):
    item: Type_of_product = await repository.create(item)

    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_product_type(
    item: Update_product_type_schema,
    product_type: Type_of_product = Depends(valid_product_type_id),
    repository: TypeOfProductRepository = Depends(Provide[Container.type_of_product_repository])
):
    await repository.update(item, product_type.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Product type successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_product_type(
    product_type: Type_of_product = Depends(valid_product_type_id),
    repository: TypeOfProductRepository = Depends(Provide[Container.type_of_product_repository])
):    
    await repository.delete(product_type.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Product type successfully removed"})