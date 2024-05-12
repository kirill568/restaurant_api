from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from app.models.dish import Dish

from app.repository import DishRepository

from app.container import Container

from app.exceptions import NotFoundError

@inject
async def valid_dish_id(id: int, repository: DishRepository = Depends(Provide[Container.dish_repository])):
    dish: Dish = await repository.get_by_id(id)
    if dish == None:
        raise NotFoundError("Dish not found")
    
    return dish