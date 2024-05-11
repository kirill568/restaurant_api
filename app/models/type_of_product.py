from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class TypeOfProduct(BaseModel):
    __tablename__ = "type_of_product"

    name = Column(String(30), index=True, nullable=False)

    products = relationship("Product", cascade="all, delete-orphan", lazy="selectin")