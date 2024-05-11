from app.schemas.base_schema import BaseSchema
from pydantic import Field 
from typing import Annotated, List
from app.schemas.address.address_schema import Address_schema

class Create_order_schema(BaseSchema):
    timestamp: Annotated[int, Field(gt=0)]
    dishes_ids: List[int]
    address: Address_schema
    client_id: Annotated[int, Field(gt=0)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "timestamp": 1656242, 
                "dishes_ids": [123, 456, 789], 
                "address": 
                    {
                        "city": "Барнаул", 
                        "street":"Рабочая", 
                        "house_number":"9", 
                        "apartment":"48"
                    }, 
                "client_id": 45
            }
        }