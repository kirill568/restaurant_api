from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from app.models.base import BaseModel

class Product(BaseModel):
    __tablename__ = "product"

    name = Column(String(30), index=True, nullable=False)
    type_of_product_id = Column(Integer, ForeignKey("type_of_product.id"))

    type_of_product = relationship("TypeOfProduct", back_populates="products")
    composition_of_dishes = relationship("CompositionOfDish", cascade="all, delete-orphan", lazy="selectin")

