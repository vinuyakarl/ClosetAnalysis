from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .base import Base

class Wear(Base):
    __tablename__ = 'wears'
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.id', ondelete="CASCADE"))
    worn_at = Column(Date, nullable=False)
    context = Column(String, nullable=True)

    item = relationship("Item", back_populates="wears")