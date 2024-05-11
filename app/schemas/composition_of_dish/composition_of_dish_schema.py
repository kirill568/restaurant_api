from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated
from datetime import time

class CompositionOfDishSchema(BaseSchema):
    id: Annotated[int, Field(gt=0)]
    product_id: Annotated[int, Field(gt=0)]
    dish_id: Annotated[int, Field(gt=0)]
    number_of_products: Annotated[int, Field(gt=0)]
    unit_of_measurement_id: Annotated[int, Field(gt=0)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "product_id": 12,
                "dish_id": 14,
                "number_of_products": 2,
                "unit_of_measurement_id": 11
            }
        }