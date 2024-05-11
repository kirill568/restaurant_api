from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class CreateClientSchema(BaseSchema):
    last_name: Annotated[str, Field(min_length=2, max_length=30)]
    first_name: Annotated[str, Field(min_length=2, max_length=30)]
    patronymic: Annotated[str, Field(min_length=2, max_length=30)]
    phone_number: Annotated[str, Field(min_length=2, max_length=20)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "last_name": "Трифонов",
                "first_name": "Данила",
                "patronymic": "Геннадьевич",
                "phone_number": "+79132182137"
            }
        }