from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from app.models.product import Product

from app.repository import ProductRepository

from app.container import Container

from app.exceptions import NotFoundError

@inject
async def valid_product_id(id: int, repository: ProductRepository = Depends(Provide[Container.product_repository])):
    product: Product = await repository.get_by_id(id)
    if product == None:
        raise NotFoundError("Product not found")
    
    return product