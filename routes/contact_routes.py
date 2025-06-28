from fastapi import APIRouter, status, HTTPException, Path
from typing import Union, Annotated, List

from schemas import contact_schemas
from cruds import contact_cruds
from database import db_session
from utils import utils


router = APIRouter(
    prefix='/messages',
    tags=["Contact - Messages"]
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=contact_schemas.ContactResponse)
async def get_messages(db: db_session, offset: Union[int, None] = 0, limit: Union[Annotated[int, Path(le=20)], None] = 20):
    messages = contact_cruds.get_messages(db, offset, limit)
    return messages


@router.post('/send-message', response_model=contact_schemas.ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_message(db: db_session, form: contact_schemas.ContactCreate):
    try:
        contact_cruds.create_message(db, form)
        utils.send_contact_email(form.name, form.email, form.message)
        return {"success": True, "message": "Message sent and saved successfuly!"}
        # return new_message
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {str(e)}"
        )
        