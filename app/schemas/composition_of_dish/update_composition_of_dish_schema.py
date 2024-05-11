from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated
from datetime import time

class Update_composition_of_dish_schema(BaseSchema):
    product_id: Annotated[int, Field(gt=0)]
    number_of_products: Annotated[int, Field(gt=0)]
    unit_of_measurement_id: Annotated[int, Field(gt=0)]
    dish_id: None = None

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "product_id": 12,
                "number_of_products": 2,
                "unit_of_measurement_id": 11
            }
        }