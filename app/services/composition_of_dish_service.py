from typing import List

from app.schemas.composition_of_dish.create_composition_of_dish_schema import Create_composition_of_dish_schema
from app.schemas.composition_of_dish.update_composition_of_dish_schema import Update_composition_of_dish_schema
from app.services.base_service import BaseService

from app.models.product import Product
from app.models.unit_of_measurement import Unit_of_measurement

from app.repository.composition_of_dish_repository import CompositionOfDishRepository
from app.repository.product_repository import ProductRepository
from app.repository.unit_of_measurement_repository import UnitOfMeasurementRepository

from app.exceptions import NotFoundError

class CompositionOfDishService(BaseService):
    def __init__(self, composition_of_dish_repository: CompositionOfDishRepository, product_repository: ProductRepository, unit_of_measurement_repository: UnitOfMeasurementRepository):
        self.composition_of_dish_repository = composition_of_dish_repository
        self.product_repository = product_repository
        self.unit_of_measurement_repository = unit_of_measurement_repository
        super().__init__(composition_of_dish_repository)

    async def create_recipe(self, dish_id: int, items: List[Create_composition_of_dish_schema]):
        for item in items:
            await self._is_product_exist(item.product_id)
            await self._is_unit_of_measurement_exist(item.unit_of_measurement_id)

        for item in items:
            item.dish_id = dish_id
            await self.composition_of_dish_repository.create(item)
    
    async def update_recipe(self, dish_id: int, items: List[Update_composition_of_dish_schema]):
        for item in items:
            await self._is_product_exist(item.product_id)
            await self._is_unit_of_measurement_exist(item.unit_of_measurement_id)

        await self.composition_of_dish_repository.delete_recipe_of_dish(dish_id)

        for item in items:
            item.dish_id = dish_id
            await self.composition_of_dish_repository.create(item)

    async def _is_product_exist(self, id: int):
        product: Product = await self.product_repository.get_by_id(id)
        if product == None:
            raise NotFoundError("Product not found")
        
        return True

    async def _is_unit_of_measurement_exist(self, id: int):
        unit_of_measurement: Unit_of_measurement = await self.unit_of_measurement_repository.get_by_id(id)
        if unit_of_measurement == None:
            raise NotFoundError("Unit of measurement not found")
        
        return True
