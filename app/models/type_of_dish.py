from sqlalchemy import Column, String
from app.models.base import BaseModel
from sqlalchemy.orm import relationship

class Type_of_dish(BaseModel):
    __tablename__ = "type_of_dish"

    name = Column(String(30), index=True, nullable=False)

    dishes = relationship("Dish", cascade="all, delete-orphan", lazy="selectin")