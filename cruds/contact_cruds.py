from datetime import date
from sqlalchemy.orm import Session

from schemas import contact_schemas
from models import models


def create_message(db: Session, message: contact_schemas.ContactCreate):
    new_message = message.dict()
    new_message.update({"created_date": date.today()})
    db_message = models.Contact(**new_message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    return db_message