from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Client(BaseModel):
    __tablename__ = "client"

    last_name = Column(String(30), index=True, nullable=False)
    first_name = Column(String(30), index=True, nullable=False)
    patronymic = Column(String(30), index=True, nullable=False)
    phone_number = Column(String(20), index=True, nullable=False)

    orders = relationship("Order", cascade="all, delete-orphan", lazy="selectin")