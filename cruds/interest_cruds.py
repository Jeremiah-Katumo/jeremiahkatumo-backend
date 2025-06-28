from datetime import date
from fastapi import Path, HTTPException, status
from sqlalchemy.orm import Session
from typing import Union, Annotated

from models import models
from schemas import interest_schemas

def get_all_interests(db: Session, offset: Union[int, None] = 0, limit: Union[Annotated[int, Path(le=10)], None] = 10):
    interests = db.query(models.Interest).order_by(models.Interest.created_date).limit(limit).offset(offset).all()
    
    if interests is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Interests Found!"
        )
        
    return interests

def get_interest_by_id(db: Session, interest_id: Annotated[int, Path(gt=0)]):
    interest = db.query(models.Interest).filter(models.Interest.id==interest_id).first()
    if interest is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No interest with id {interest_id} found!"
        )
    return interest
        
def create_interest(db: Session, interest: interest_schemas.InterestCreate):
    new_interest = interest.dict()
    interest_in_db = db.query(models.Interest).filter(models.Interest.title==interest.title).first()
    if interest_in_db != None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Interest with title {interest.title} already exists!"
        )
        
    new_interest.update({"created_date": date.today()})
    db_interest = models.Interest(**new_interest)
    db.add(db_interest)
    db.commit()
    db.refresh(db_interest)
    
    return db_interest

def update_interest(db: Session, interest_id: Annotated[int, Path(gt=0)], interest: interest_schemas.InterestCreate):
    req_interest = interest.dict()
    updated_interest = db.query(models.Interest).filter(models.Interest.id==interest_id).first()
    if updated_interest is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Interest with id {interest_id} does not exist!"
        )
        
    for key, val in req_interest.items():
        if val is not None:
            if key == 'interests' and updated_interest.interests is not None:
                setattr(updated_interest, key, list(set(val + updated_interest.interests)))
            else:
                setattr(updated_interest, key, val)
                
    updated_interest.updated_date = date.today()
    
    db.commit()
    db.refresh(updated_interest)
    
    return updated_interest

def delete_interest(db: Session, interest_id: Annotated[int, Path(gt=0)]):
    interest = db.query(models.Interest).filter(models.Interest.id==interest_id).first()
    if interest is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Interest with id {interest_id} found!"
        )
        
    db.delete(interest)
    db.commit()
    
    return interest