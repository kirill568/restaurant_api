from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Composition_of_dish(BaseModel):
    __tablename__ = "composition_of_dish"

    product_id = Column(Integer, ForeignKey("product.id"))
    dish_id = Column(Integer, ForeignKey("dish.id"))
    number_of_products = Column(Float(), index=True, nullable=False)
    unit_of_measurement_id = Column(Integer, ForeignKey("unit_of_measurement.id"))

    product = relationship("Product", back_populates="composition_of_dishes")
    dish = relationship("Dish", back_populates="composition_of_dishes")
    unit_of_measurement = relationship("Unit_of_measurement", back_populates="composition_of_dishes")