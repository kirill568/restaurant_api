from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class Unit_of_measurement_schema(BaseSchema):
    id: Annotated[int, Field(gt=0)]
    name: Annotated[str, Field(min_length=2, max_length=100)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "кг."
            }
        }