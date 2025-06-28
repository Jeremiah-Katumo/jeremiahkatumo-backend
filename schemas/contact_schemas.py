from pydantic import BaseModel, EmailStr

class ContactBase(BaseModel):
    id: int
        
class ContactCreate(ContactBase):
    name: str
    email: EmailStr
    message: str
    
class ContactResponse(ContactBase):
    name: str
    email: EmailStr
    message: str
    
    class Config:
        from_attributes = True