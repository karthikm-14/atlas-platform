from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.item import Item


router = APIRouter()

@router.get("/items")
def list_items(db: Session = Depends(get_db)):
    return db.query(Item).all()


@router.post("/items")
def create_item(name: str, db: Session = Depends(get_db)):
    item = Item(name=name)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
