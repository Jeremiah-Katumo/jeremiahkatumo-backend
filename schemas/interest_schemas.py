from pydantic import BaseModel
from datetime import date, datetime
from typing import Union

class InterestBase(BaseModel):
    icon_class: str
    title: str
    description: str
        
class InterestCreate(InterestBase):
    pass

class InterestResponse(BaseModel):
    icon_class: str
    title: str
    description: str
    
    class Config:
        from_attributes = True
        