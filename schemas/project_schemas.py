from pydantic import BaseModel
from datetime import datetime, date
from typing import Union, List
from enum import Enum


class ImageNumber(str, Enum):
    one = "one"
    two = "two"

class ProjectBase(BaseModel):
    id: int
    image_number: ImageNumber
    title: str
    category: str
    link: str
    image_link: str

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(BaseModel):
    image_number: str
    title: str
    category: str
    link: str
    image_link: str
    
    class Config:
        from_attributes=True
