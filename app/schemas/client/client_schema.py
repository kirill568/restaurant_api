from pydantic import BaseModel
from pydantic import Field
from typing import Annotated

class Client_schema(BaseModel):
    id: Annotated[int, Field(gt=0)]
    last_name: Annotated[str, Field(min_length=2, max_length=30)]
    first_name: Annotated[str, Field(min_length=2, max_length=30)]
    patronymic: Annotated[str, Field(min_length=2, max_length=30)]
    phone_number: Annotated[str, Field(min_length=2, max_length=20)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "last_name": "Трифонов",
                "first_name": "Данила",
                "patronymic": "Геннадьевич",
                "phone_number": "+79132182137"
            }
        }