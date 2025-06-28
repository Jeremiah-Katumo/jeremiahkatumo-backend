from fastapi import APIRouter, status

from schemas import contact_schemas
from cruds import contact_cruds
from database import db_session

router = APIRouter(
    prefix='/contacts',
    tags=["Contacts"]
)

router.post('/', response_model=contact_schemas.ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_message(db: db_session, message: contact_schemas.ContactCreate):
    new_message = contact_cruds.create_message(db, message)
    return new_message