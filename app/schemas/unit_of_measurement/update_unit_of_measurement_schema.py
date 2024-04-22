from pydantic import BaseModel
from pydantic import Field
from typing import Annotated

class Update_unit_of_measurement_schema(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=100)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "кг."
            }
        }