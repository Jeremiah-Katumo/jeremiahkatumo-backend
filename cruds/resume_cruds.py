from fastapi import Path, status, HTTPException
from typing import Annotated, Union
from sqlalchemy.orm import Session

from schemas import resume_schemas
from models import models

def get_resumes(db: Session, offset: Union[int, None] = 0, limit: Union[Annotated[int, Path(le=20)], None] = 20):
    resumes = db.query(models.Resume).order_by(models.Resume.created_date.desc()).limit(limit).offset(offset).all()
    if resumes == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Resume Found!"
        )
    return resumes

def get_resume_by_id(db: Session, resume_id: Annotated[int, Path(gt=0)]):
    resume = db.query(models.Resume).filter(models.Resume.id==resume_id).first()
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No resume with id {resume_id} found!"
        )
    return resume

