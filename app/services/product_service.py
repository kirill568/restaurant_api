from app.services.base_service import BaseService

from app.models.product import Product
from app.models.type_of_product import TypeOfProduct

from app.repository.product_repository import ProductRepository
from app.repository.type_of_product_repository import TypeOfProductRepository

from app.schemas.product.create_product_schema import CreateProductSchema
from app.schemas.product.update_product_schema import UpdateProductSchema

from app.exceptions import NotFoundError

class ProductService(BaseService):
    def __init__(self, product_repository: ProductRepository, type_of_product_repository: TypeOfProductRepository):
        self.product_repository = product_repository
        self.type_of_product_repository = type_of_product_repository
        super().__init__(product_repository)

    async def create_product(self, item: CreateProductSchema):        
        await self._is_product_type_exist(item.type_of_product_id)

        return await self.product_repository.create(item)
    
    async def update_product(self, item: UpdateProductSchema, id: int):        
        await self._is_product_type_exist(item.type_of_product_id)

        return await self.product_repository.update(item, id)
    
    async def _is_product_type_exist(self, id: int):
        product_type: TypeOfProduct = await self.type_of_product_repository.get_by_id(id)
        if product_type is None:
            raise NotFoundError("Product type not found")
        
        return True