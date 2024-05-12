from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from app.models.type_of_product import TypeOfProduct

from app.repository import TypeOfProductRepository

from app.container import Container

from app.exceptions import NotFoundError

@inject
async def valid_product_type_id(id: int, repository: TypeOfProductRepository = Depends(Provide[Container.type_of_product_repository])):
    product_type: TypeOfProduct = await repository.get_by_id(id)
    if product_type == None:
        raise NotFoundError("Product type not found")
    
    return product_type