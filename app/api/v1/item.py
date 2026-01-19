from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemResponse


router = APIRouter()

@router.get("/items", response_model=list[ItemResponse])
def list_items(db: Session = Depends(get_db)):
    return db.query(Item).all()


@router.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
