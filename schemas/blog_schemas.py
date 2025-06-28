from pydantic import BaseModel
from datetime import datetime, date

class BlogSchema(BaseModel):
    id: int
    published_at: datetime
    link: str
    author: str
    title: str
    description: str

    class Config:
        from_attributes = True