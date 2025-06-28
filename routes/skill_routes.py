from fastapi import APIRouter, status, Path, Depends
from typing import Annotated, Union, List

from schemas import skill_schemas
from cruds import skill_cruds
from database import db_session

router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)

@router.get("/{skill_id}", response_model=skill_schemas.SkillResponse, status_code=status.HTTP_200_OK)
async def get_skill(db: db_session, skill_id: Annotated[int, Path(gt=0)]):
    skill = skill_cruds.get_skill_by_id(db, skill_id)
    return skill

@router.get("/", response_model=List[skill_schemas.SkillResponse], status_code=status.HTTP_200_OK)
async def get_skills(db: db_session, offset: Union[int, None] = 0, limit: Union[Annotated[int, Path(le=20)], None] = 20):
    skills = skill_cruds.get_all_skills(db=db, offset=offset, limit=limit)
    return skills

@router.post("/", response_model=skill_schemas.SkillResponse, status_code=status.HTTP_201_CREATED)
async def create_skill(db: db_session, skill: skill_schemas.SkillCreate):
    new_skill = skill_cruds.create_skill(db, skill)
    return new_skill

@router.patch('/{skill_id}', response_model=skill_schemas.SkillResponse, status_code=status.HTTP_201_CREATED)
async def update_skill(db: db_session, skill_id: Annotated[int, Path(gt=0)], skill: skill_schemas.SkillCreate):
    updated_skill = skill_cruds.update_skill(db, skill_id, skill)
    return updated_skill

@router.delete('/{skill_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_skill(db: db_session, skill_id: Annotated[int, Path(gt=0)]):
    deleted_skill = skill_cruds.delete_skill(db, skill_id)
    return deleted_skill
