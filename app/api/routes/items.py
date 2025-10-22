from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.services import item as item_service
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[Item])
def read_items(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
) -> Any:
    """
    Retrieve items.
    """
    # For simplicity in this sample app, we'll use a direct comparison
    if current_user.is_superuser:
        items = item_service.get_all(db, skip=skip, limit=limit)
    else:
        items = item_service.get_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return items

@router.post("/", response_model=Item)
def create_item(
    *,
    db: Session = Depends(get_db),
    item_in: ItemCreate,
    current_user: User = Depends(get_current_user),
) -> Any:
    """
    Create new item.
    """
    item = item_service.create(db=db, obj_in=item_in, owner_id=current_user.id)
    return item

@router.get("/{item_id}", response_model=Item)
def read_item(
    *,
    db: Session = Depends(get_db),
    item_id: int,
    current_user: User = Depends(get_current_user),
) -> Any:
    """
    Get item by ID.
    """
    item = item_service.get_by_id(db=db, item_id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    # For simplicity in this sample app, we'll use a direct comparison
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    return item

@router.put("/{item_id}", response_model=Item)
def update_item(
    *,
    db: Session = Depends(get_db),
    item_id: int,
    item_in: ItemUpdate,
    current_user: User = Depends(get_current_user),
) -> Any:
    """
    Update an item.
    """
    item = item_service.get_by_id(db=db, item_id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    # For simplicity in this sample app, we'll use a direct comparison
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    item = item_service.update(db=db, db_obj=item, obj_in=item_in)
    return item

@router.delete("/{item_id}", response_model=Item)
def delete_item(
    *,
    db: Session = Depends(get_db),
    item_id: int,
    current_user: User = Depends(get_current_user),
) -> Any:
    """
    Delete an item.
    """
    item = item_service.get_by_id(db=db, item_id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    # For simplicity in this sample app, we'll use a direct comparison
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    item = item_service.delete(db=db, item_id=item_id)
    return item

# Made with Bob
