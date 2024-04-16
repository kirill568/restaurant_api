from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from app.models.base import BaseModel

class Product(BaseModel):
    __tablename__ = "product"

    name_of_product = Column(String(30), index=True, nullable=False)
    type_of_product_id = Column(Integer, ForeignKey("type_of_product.id"))

    type_of_product = relationship("Type_of_product", back_populates="products")

    composition_of_dishes = relationship("Composition_of_dish", cascade="all, delete-orphan", lazy="selectin")

