from pydantic import BaseModel

class ServiceBase(BaseModel):
    category: str
    icon: str
    title: str

class ServiceCreate(ServiceBase):
    pass

class ServiceResponse(BaseModel):
    category: str
    icon: str
    title: str
    
    class Config:
        from_attributes = True