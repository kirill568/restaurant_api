from pydantic import BaseModel
from pydantic import Field
from typing import Annotated
from datetime import time

class Create_composition_of_dish_schema(BaseModel):
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