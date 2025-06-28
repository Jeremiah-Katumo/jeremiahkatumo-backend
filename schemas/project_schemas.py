from pydantic import BaseModel
from datetime import datetime, date
from typing import Union, List

class ProjectSchema(BaseModel):
    id: int
    imageNumber: bool
    title: str
    category: str
    link: str
    imageLink: str

    class Config:
        from_attributes = True
