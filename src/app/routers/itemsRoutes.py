from fastapi import APIRouter, Depends, HTTPException
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
@router.get("/{id}", response_model=itemSchema.ItemResponse)
async def read_item(id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Delete an item
@router.delete("/{id}", response_model=itemSchema.ItemResponse)
async def delete_item(id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item