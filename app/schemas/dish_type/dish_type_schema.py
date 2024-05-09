from pydantic import BaseModel
from pydantic import Field
from typing import Annotated

class Dish_type_schema(BaseModel):
    id: Annotated[int, Field(gt=0)]
    name: Annotated[str, Field(min_length=2, max_length=100)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Десерт"
            }
        }