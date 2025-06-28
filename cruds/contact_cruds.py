from datetime import date
from sqlalchemy.orm import Session
from typing  import Annotated, List, Union
from fastapi import Path, HTTPException, status

from schemas import contact_schemas
from models import models


def create_message(db: Session, form: contact_schemas.ContactCreate):
    new_message = form.dict()
    new_message.update({"created_date": date.today()})
    db_message = models.Contact(**new_message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def save_message(db: Session, form: contact_schemas.ContactCreate):
    new_message = models.Contact(
        name=form.name,
        email=form.email,
        message=form.message,
        created_date=date.today()
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

def get_messages(db: Session, offset: Union[int, None] = 0, limit: Union[Annotated[int, Path(le=10)], None] = 10):
    messages = db.query(models.Contact) \
        .order_by(models.Contact.created_date) \
            .limit(limit).offset(offset).all()
            
    if messages is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No messages found!"
        )