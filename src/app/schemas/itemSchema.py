from datetime import date, datetime

from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    category: str
    brand: str
    purchase_price: float
    purchase_date: date
    tags: list[str]

class ItemCreate(ItemBase):
    pass

class ItemResponse(BaseModel):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True