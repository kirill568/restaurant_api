from pydantic import BaseModel
from pydantic import Field
from typing import Annotated

class Address_schema(BaseModel):
    city: Annotated[str, Field(min_length=2, max_length=100)]
    street: Annotated[str, Field(min_length=2, max_length=100)]
    house_number: Annotated[str, Field(min_length=2, max_length=10)]
    apartment: Annotated[int, Field(gt=0)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "city": "Барнаул",
                "street": "Рабочая",
                "house_number": "9",
                "apartment": 48
            }
        }