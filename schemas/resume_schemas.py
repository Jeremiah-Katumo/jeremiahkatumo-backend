from pydantic import BaseModel
from datetime import date, datetime

class ResumeBase(BaseModel):
    id: int
    start_year: str
    completion_year: str
    title: str
    school: str
    description: str
        
class ResumeCreate(ResumeBase):
    pass

class ResumeResponse(BaseModel):
    start_year: str
    completion_year: str
    title: str
    school: str
    description: str
    
    class Config:
        from_attributes = True