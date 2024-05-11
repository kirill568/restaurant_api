from pydantic import BaseModel
from pydantic import Field 
from datetime import datetime
from typing import Annotated, List
from app.schemas.address.address_schema import Address_schema

class Create_orm_entity_order_schema(BaseModel):
    date: datetime
    client_id: Annotated[int, Field(gt=0)]