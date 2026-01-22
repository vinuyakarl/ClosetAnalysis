from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.core import get_db

from app.models import Wear, Item
from app.schemas import wearSchema

router = APIRouter()


# Creates a wear instance
@router.post("/", response_model=wearSchema.WearResponse)
async def create_wear(wear: wearSchema.WearCreate, db: Session = Depends(get_db)):
    # Check existence of object BEFORE adding to DB
    item = db.query(Item).get(wear.item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_wear = Wear(**wear.dict())
    db.add(db_wear)
    db.commit()
    db.refresh(db_wear)
    return db_wear