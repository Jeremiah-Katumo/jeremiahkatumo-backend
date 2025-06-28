from pydantic import BaseModel
from datetime import date, datetime

class ResumeSchema(BaseModel):
    id: int
    completion_date: date
    title: str
    school: str
    description: str

    class Config:
        from_attributes = True