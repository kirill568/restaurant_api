from app.schemas.base_schema import BaseSchema
from pydantic import Field 
from typing import Annotated, List

class CreateBillSchema(BaseSchema):
    order_id: Annotated[int, Field(gt=0)]
    dish_id: Annotated[int, Field(gt=0)]