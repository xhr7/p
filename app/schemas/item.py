from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Shared properties
class ItemBase(BaseModel):
    description: Optional[str] = None
    is_active: bool = True

# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str

# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass

# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    title: str  # This is fine as it's a required field in the DB
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Properties to return to client
class Item(ItemInDBBase):
    pass

# Properties stored in DB
class ItemInDB(ItemInDBBase):
    pass

# Made with Bob
