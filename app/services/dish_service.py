from app.services.base_service import BaseService

from app.models.dish import Dish
from app.models.type_of_dish import Type_of_dish

from app.repository.dish_repository import DishRepository
from app.repository.type_of_dish_repository import TypeOfDishRepository

from app.schemas.dish.create_dish_schema import Create_dish_schema
from app.schemas.dish.update_dish_schema import Update_dish_schema

from app.exceptions import NotFoundError

class DishService(BaseService):
    def __init__(self, dish_repository: DishRepository, type_of_dish_repository: TypeOfDishRepository):
        self.dish_repository = dish_repository
        self.type_of_dish_repository = type_of_dish_repository
        super().__init__(dish_repository)

    async def create_dish(self, item: Create_dish_schema):        
        await self._is_dish_type_exist(item.type_of_dish_id)

        return await self.dish_repository.create(item)
    
    async def update_dish(self, item: Update_dish_schema, id: int):        
        await self._is_dish_type_exist(item.type_of_dish_id)

        return await self.dish_repository.update(item, id)
    
    async def _is_dish_type_exist(self, id: int):
        dish_type: Type_of_dish = await self.type_of_dish_repository.get_by_id(id)
        if dish_type is None:
            raise NotFoundError("Dish type not found")
        
        return True