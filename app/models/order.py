from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Order(BaseModel):
    __tablename__ = "order"

    client_id = Column(Integer, ForeignKey("client.id"))
    date = Column(DateTime, index=True, nullable=False)

    client = relationship("Client", back_populates="orders")

    bills = relationship("Bill", cascade="all, delete-orphan", lazy="selectin")