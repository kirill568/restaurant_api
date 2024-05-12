from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from app.models.type_of_dish import TypeOfDish

from app.repository import TypeOfDishRepository

from app.container import Container

from app.exceptions import NotFoundError

@inject
async def valid_dish_type_id(id: int, repository: TypeOfDishRepository = Depends(Provide[Container.type_of_dish_repository])):
    dish_type: TypeOfDish = await repository.get_by_id(id)
    if dish_type == None:
        raise NotFoundError("Dish type not found")
    
    return dish_type