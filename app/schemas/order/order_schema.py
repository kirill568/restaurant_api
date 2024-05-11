from app.schemas.base_schema import BaseSchema
from pydantic import Field 
from typing import Annotated, List
from app.schemas.address.address_schema import Address_schema

class Order_schema(BaseSchema):
    id: Annotated[int, Field(gt=0)]
    timestamp: Annotated[int, Field(gt=0)]
    dishes_ids: List[int]
    client_id: Annotated[int, Field(gt=0)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "timestamp": 1656242, 
                "dishes_ids": [123, 456, 789], 
                "client_id": 45
            }
        }