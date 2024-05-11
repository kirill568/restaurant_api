from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class UnitOfMeasurement(BaseModel):
    __tablename__ = "unit_of_measurement"

    name = Column(String(100), index=True, nullable=False)
    
    composition_of_dishes = relationship("CompositionOfDish", cascade="all, delete-orphan", lazy="selectin")