from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app.database.core import get_db

from app.models import Item
from app.schemas import itemSchema

router = APIRouter()


# Gets all the items
@router.get("/", response_model=Page[itemSchema.ItemResponse])
async def read_items(db: Session = Depends(get_db)):
    return paginate(db.query(Item))

# Creates an item
@router.post("/", response_model=itemSchema.ItemResponse)
async def create_item(item: itemSchema.ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Get one item

# Delete an item