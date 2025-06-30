from fastapi import APIRouter, status, Path
from typing import Annotated, List, Union

from database import db_session
from schemas import blog_schemas
from cruds import blog_cruds

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

@router.get('/', response_model=List[blog_schemas.BlogResponse], status_code=status.HTTP_200_OK)
async def get_blogs(db: db_session, offset: Union[int, None] = 0,
                    limit: Union[Annotated[int, Path(le=10)], None] = 10):
    return blog_cruds.get_blogs(db, offset, limit)

@router.get('/{blog_id}', response_model=blog_schemas.BlogResponse, status_code=status.HTTP_200_OK)
async def get_blog_by_id(db: db_session, blog_id: Annotated[int, Path(gt=0)]):
    return blog_cruds.get_blog_by_id(db, blog_id)