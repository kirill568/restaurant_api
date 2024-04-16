from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Unit_of_measurement(BaseModel):
    __tablename__ = "unit_of_measurement"

    name_unit_of_measurement = Column(String(100), index=True, nullable=False)

    composition_of_dishes = relationship("Composition_of_dish", cascade="all, delete-orphan", lazy="selectin")