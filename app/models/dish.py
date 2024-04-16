from sqlalchemy import Column, String, Float, Time, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Dish(BaseModel):
    __tablename__ = "dish"

    name = Column(String(100), index=True, nullable=False)
    cost = Column(Float(), index=True, nullable=False)
    weight = Column(Float(), index=True, nullable=False)
    calories = Column(Float(), index=True, nullable=False)
    cooking_time = Column(Time(), index=True, nullable=False)
    type_of_dish_id =  Column(Integer, ForeignKey("type_of_product.id"))

    type_of_dish = relationship("Type_of_dish", back_populates="dishes")

    composition_of_dishes = relationship("Composition_of_dish", cascade="all, delete-orphan", lazy="selectin")
    bills = relationship("Bill", cascade="all, delete-orphan", lazy="selectin")