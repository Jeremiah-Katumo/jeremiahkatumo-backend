from pydantic import BaseModel

class InterestBase(BaseModel):
    id: int
        
class InterestCreate(InterestBase):
    icon_class: str
    title: str
    description: str
    
class InterestResponse(InterestBase):
    icon_class: str
    title: str
    description: str
    
    class Config:
        from_attributes = True
        