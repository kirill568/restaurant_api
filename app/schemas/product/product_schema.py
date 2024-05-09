from pydantic import BaseModel
from pydantic import Field
from typing import Annotated

class Product_schema(BaseModel):
    id: Annotated[int, Field(gt=0)]
    name: Annotated[str, Field(min_length=2, max_length=100)]
    type_of_product_id: Annotated[int, Field(gt=0)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Яблоко",
                "type_of_product_id": 123
            }
        }