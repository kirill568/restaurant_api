from pydantic import BaseModel
from pydantic import Field
from typing import Annotated

class Create_dish_type_schema(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=100)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "Десерт"
            }
        }