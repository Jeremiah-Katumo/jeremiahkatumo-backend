from pydantic import BaseModel

class ServiceSchema(BaseModel):
    id: int
    category: str
    icon: str
    title: str

    class Config:
        # orm_mode = True
        from_attributes = True