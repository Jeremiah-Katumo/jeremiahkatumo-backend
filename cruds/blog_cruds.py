from sqlalchemy.orm import Session
from fastapi import Path, HTTPException, status
from typing import Annotated, Union

from models import models

def get_blogs(db: Session, offset: Union[int, None] = 0,
              limit: Union[Annotated[int, Path(le=10)], None] = 10) -> models.Blog:
    blogs = db.query(models.Blog).order_by(models.Blog.created_date.desc()) \
        .limit(limit).offset(offset).all()
    if blogs is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No blog post found!"
        )
    return blogs

def get_blog_by_id(db: Session, blog_id: Annotated[int, Path(gt=0)]):
    blog = db.query(models.Blog).filter(models.Blog.id==blog_id).first()
    if blog is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No blog found with id {blog_id}"
        )
    return blog