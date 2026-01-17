from sqlalchemy import Column, Integer, String, Float, ARRAY, DateTime, Date, func
from sqlalchemy.orm import relationship

from .base import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    brand = Column(String, nullable=True)
    purchase_price = Column(Float, nullable=True)
    purchase_date = Column(Date, nullable=True)
    tags = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    wears = relationship("Wear", back_populates="item", cascade="all, delete", passive_deletes=True)

