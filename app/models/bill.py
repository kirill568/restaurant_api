from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Bill(BaseModel):
    __tablename__ = "bill"

    order_id = Column(Integer, ForeignKey("order.id"))
    dish_id = Column(Integer, ForeignKey("dish.id"))

    order = relationship("Order", back_populates="bills")
    dish = relationship("Dish", back_populates="bills")