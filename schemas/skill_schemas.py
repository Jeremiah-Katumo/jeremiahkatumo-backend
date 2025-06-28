from pydantic import BaseModel
from datetime import date, datetime
from typing import Union

class SkillBase(BaseModel):
    id: int
    created_date: datetime
    updated_date: Union[date, None] = None
    created_by: Union[int, None] = None
    updated_by: Union[int, None] = None
        
class SkillCreate(SkillBase):
    icon_class: str
    title: str
    
class SkillResponse(BaseModel):
    icon_class: str
    title: str
    
    class Config:
        from_attributes = True
        