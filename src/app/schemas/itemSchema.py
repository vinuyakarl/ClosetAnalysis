from datetime import date, datetime
from typing import List

from pydantic import BaseModel

from app.schemas.wearSchema import WearResponse


class ItemBase(BaseModel):
    name: str
    category: str
    brand: str
    purchase_price: float
    purchase_date: date
    tags: list[str]

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    created_at: datetime
    wears: List[WearResponse] = []

    class Config:
        from_attributes = True