from pydantic import BaseModel
from pydantic import Field 
from typing import Annotated, List

class Create_bill_schema(BaseModel):
    order_id: Annotated[int, Field(gt=0)]
    dish_id: Annotated[int, Field(gt=0)]