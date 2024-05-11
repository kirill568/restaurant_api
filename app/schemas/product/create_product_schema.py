from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class Create_product_schema(BaseSchema):
    name: Annotated[str, Field(min_length=2, max_length=100)]
    type_of_product_id: Annotated[int, Field(gt=0)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "Яблоко",
                "type_of_product_id": 123
            }
        }