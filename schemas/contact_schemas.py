from pydantic import BaseModel, EmailStr
import enum
from datetime import date, datetime
from typing import Union

class ContactBase(BaseModel):
    # id: int
    updated_date: Union[date, None] = None
    created_by: Union[int, None] = None
    updated_by: Union[int, None] = None
        
class ContactCreate(ContactBase):
    name: str
    email: EmailStr
    message: str
    
class ContactResponse(ContactBase):
    id: int
    name: str
    email: EmailStr
    message: str
    status: str
    created_date: datetime
    
    class Config:
        from_attributes = True
        
        
class MessageStatus(str, enum.Enum):
    pending = "pending"
    seen = "seen"
    responded = "responded"