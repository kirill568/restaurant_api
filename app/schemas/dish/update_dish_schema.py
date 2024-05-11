from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated
from datetime import time

class UpdateDishSchema(BaseSchema):
    name: Annotated[str, Field(min_length=2, max_length=100)]
    cost: Annotated[float, Field(gt=0.0)]
    weight: Annotated[float, Field(gt=0.0)]
    calories: Annotated[float, Field(gt=0.0)]
    cooking_time: time
    type_of_dish_id: Annotated[int, Field(gt=0)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "Десерт",
                "price": 123.05,
                "weight": 78.00,
                "caloric_value": 775,
                "cooking_time": "20:00",
                "dish_type_id": 123
            }
        }