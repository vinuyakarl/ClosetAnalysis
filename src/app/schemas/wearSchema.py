from datetime import date
from pydantic import BaseModel


class Wear(BaseModel):
    id: int
    item_id: int
    worn_at: date
    context: str
