from fastapi import APIRouter, Path, status
from typing import Union, Annotated, List

from schemas import project_schemas
from cruds import project_cruds
from models import models
from database import db_session
from utils import utils

router = APIRouter(
    prefix='/projects',
    tags=["Projects"]
)


@router.get('/', response_model=List[project_schemas.ProjectResponse], status_code=status.HTTP_200_OK)
async def get_projects(db: db_session, offset: Union[int, None] = 0,
                       limit: Union[Annotated[int, Path(le=10)], None] = 10):
    projects = project_cruds.get_projects(db, offset, limit)
    return projects


@router.get('/{project_id}', response_model=project_schemas.ProjectResponse, 
            status_code=status.HTTP_200_OK)
async def get_project_by_id(db: db_session, project_id: Annotated[int, Path(gt=0)]):
    return project_cruds.get_project_by_id(project_id, db)


@router.post("/hires", status_code=status.HTTP_201_CREATED)
def create_hire(hire: project_schemas.HireCreate, db: db_session):
    new_hire = project_cruds.hire_me(db, hire)

    try:
        utils.send_email(hire)
        # utils.send_sms(hire.phone, f"Hi {hire.name}, thanks for reaching out! We'll get back to you shortly.")
    except Exception as e:
        print("Notification error:", e)

    return {"message": "Hire request submitted successfully!", "hire": new_hire}
