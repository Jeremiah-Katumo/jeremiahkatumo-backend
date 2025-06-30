from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class BlogBase(BaseModel):
    published_at: Optional[datetime] = None
    link: str
    author: str
    title: str
    description: str

class BlogCreate(BlogBase):
    pass

class BlogResponse(BaseModel):
    published_at: Optional[datetime] = None
    link: str
    author: str
    title: str
    description: str
    
    class Config:
        from_attributes = True