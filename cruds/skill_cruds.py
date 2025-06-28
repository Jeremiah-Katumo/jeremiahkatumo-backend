from datetime import date
from fastapi import Path, HTTPException, status
from sqlalchemy.orm import Session
from typing import Union, Annotated

from models import models
from schemas import interest_schemas

def get_all_skills(db: Session, offset: Union[int, None] = 0, limit: Union[Annotated[int, Path(le=10)], None] = 10):
    skills = db.query(models.Skill).order_by(models.Skill.created_date).limit(limit).offset(offset).all()
    
    if skills is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Skills Found!"
        )
        
    return skills

def get_skill_by_id(db: Session, skill_id: Annotated[int, Path(gt=0)]):
    skill = db.query(models.Skill).filter(models.Skill.id==skill_id).first()
    if skill is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No skill with id {skill_id} found!"
        )
        
def create_skill(db: Session, skill: interest_schemas.SkillCreate):
    new_skill = skill.dict()
    skill_in_db = db.query(models.Skill).filter(models.Skill.title==skill.title).first()
    if skill_in_db != None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Skill with title {skill.title} already exists!"
        )
        
    new_skill.update({"created_date": date.today()})
    db_skill = models.Skill(**new_skill)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    
    return db_skill

def update_skill(db: Session, skill_id: Annotated[int, Path(gt=0)], skill: interest_schemas.SkillCreate):
    req_skill = skill.dict()
    updated_skill = db.query(models.Skill).filter(models.Skill.id==skill_id).first()
    if updated_skill is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Skill with id {skill_id} does not exist!"
        )
        
    for key, val in req_skill.items():
        if val is not None:
            if key == 'skills' and updated_skill.skills is not None:
                setattr(updated_skill, key, list(set(val + updated_skill.skills)))
            else:
                setattr(updated_skill, key, val)
                
    updated_skill.updated_date = date.today()
    
    db.commit()
    db.refresh(updated_skill)
    
    return updated_skill

def delete_skill(db: Session, skill_id: Annotated[int, Path(gt=0)]):
    skill = db.query(models.Skill).filter(models.Skill.id==skill_id).first()
    if skill is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No skill with id {skill_id} found!"
        )
        
    db.delete(skill)
    db.commit()
    
    return skill