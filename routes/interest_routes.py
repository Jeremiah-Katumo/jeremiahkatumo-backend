from fastapi import APIRouter, status, Path, Depends
from typing import Annotated, Union, List

from schemas import interest_schemas
from cruds import interest_cruds
from database import db_session

router = APIRouter(
    prefix="/interests",
    tags=["Interests"]
)

@router.get("/{interest_id}", response_model=interest_schemas.InterestResponse, status_code=status.HTTP_200_OK)
async def get_interest(db: db_session, interest_id: Annotated[int, Path(gt=0)]):
    interest = interest_cruds.get_interest_by_id(db, interest_id)
    return interest

@router.get("/", response_model=List[interest_schemas.InterestResponse], status_code=status.HTTP_200_OK)
async def get_interests(db: db_session, offset: Union[int, None] = 0, limit: Union[Annotated[int, Path(le=20)], None] = 20):
    interests = interest_cruds.get_all_interests(db=db, offset=offset, limit=limit)
    return interests

@router.post("/", response_model=interest_schemas.InterestResponse, status_code=status.HTTP_201_CREATED)
async def create_interest(db: db_session, interest: interest_schemas.InterestCreate):
    new_interest = interest_cruds.create_interest(db, interest)
    return new_interest

@router.patch('/{interest_id}', response_model=interest_schemas.InterestResponse, status_code=status.HTTP_201_CREATED)
async def update_skill(db: db_session, interest_id: Annotated[int, Path(gt=0)], interest: interest_schemas.InterestCreate):
    updated_interest = interest_cruds.update_interest(db, interest_id, interest)
    return updated_interest

@router.delete('/{interest_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_skill(db: db_session, interest_id: Annotated[int, Path(gt=0)]):
    deleted_interest = interest_cruds.delete_interest(db, interest_id)
    return deleted_interest
