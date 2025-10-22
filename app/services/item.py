from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.item import Item
from app.models.user import User
from app.schemas.item import ItemCreate, ItemUpdate

def get_by_id(db: Session, item_id: int) -> Optional[Item]:
    """
    Get an item by ID
    """
    return db.query(Item).filter(Item.id == item_id).first()

def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    """
    Get all items
    """
    return db.query(Item).offset(skip).limit(limit).all()

def get_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 100) -> List[Item]:
    """
    Get items by owner
    """
    return db.query(Item).filter(Item.owner_id == owner_id).offset(skip).limit(limit).all()

def create(db: Session, obj_in: ItemCreate, owner_id: int) -> Item:
    """
    Create a new item
    """
    db_obj = Item(
        title=obj_in.title,
        description=obj_in.description,
        is_active=obj_in.is_active,
        owner_id=owner_id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(db: Session, db_obj: Item, obj_in: ItemUpdate) -> Item:
    """
    Update an item
    """
    update_data = obj_in.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete(db: Session, item_id: int) -> Item:
    """
    Delete an item
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item

# Made with Bob
