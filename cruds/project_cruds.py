from sqlalchemy.orm import Session
from typing import Union, Annotated
from fastapi import Path, status, HTTPException

from models import models
from schemas import project_schemas

def get_projects(db: Session, offset: Union[int, None] = 0,
        limit: Union[Annotated[int, Path(le=10)], None] = 10
    ) -> models.Project:
    projects = db.query(models.Project).order_by(models.Project.created_date.desc()) \
        .limit(limit).offset(offset).all()
        
    if not projects:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No projects found!"
        )
    return projects

def get_project_by_id(project_id: Annotated[int, Path(gt=0)], db: Session) -> models.Project:
    project = db.query(models.Project).filter(models.Project.id==project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No project with id {project_id} found!"
        )
    return project