from datetime import date
from pydantic import BaseModel


class WearBase(BaseModel):
    item_id: int
    worn_at: date
    context: str

class WearCreate(WearBase):
    pass

class WearResponse(WearBase):
    id: int