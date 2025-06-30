from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session
from typing import List, Union, Annotated

from database import db_session
from schemas import service_schemas
from cruds import service_cruds


router = APIRouter(
    prefix="/services", 
    tags=["Services"]
)


@router.get("/{category}", response_model=List[service_schemas.ServiceResponse])
async def fetch_services_by_category(
    db: db_session,
    category: str,
    offset: Union[int, None] = 0, 
    limit: Union[Annotated[int, Path(le=10)], None] = 10
):
    return service_cruds.get_services_by_category(category, db, offset, limit)

@router.get("/{category}/{service_id}", response_model=service_schemas.ServiceResponse)
async def fetch_service_by_id(
    db: db_session,
    category: str,
    service_id: int = Path(..., gt=0)
):
    return service_cruds.get_service_by_id(category, service_id, db)
