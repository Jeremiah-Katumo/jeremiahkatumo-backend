from fastapi import HTTPException, status, Path
from sqlalchemy.orm import Session
from typing import Optional, List

from models import models


def get_services_by_category(category: str, db: Session, offset: int = 0, limit: int = 3) -> List[models.Service]:
    if category not in ("top", "bottom"):
        raise HTTPException(status_code=400, detail="Category must be 'top' or 'bottom'")

    query = db.query(models.Service).filter(models.Service.category == category)

    if category == "top":
        query = query.order_by(models.Service.created_date.desc())
    else:
        query = query.order_by(models.Service.created_by.desc())

    services = query.offset(offset).limit(limit).all()

    if not services:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No {category} services found"
        )

    return services


def get_service_by_id(category: str, service_id: int, db: Session) -> models.Service:
    if category not in ("top", "bottom"):
        raise HTTPException(status_code=400, detail="Category must be 'top' or 'bottom'")

    service = db.query(models.Service) \
        .filter(models.Service.category == category, models.Service.id == service_id) \
        .first()

    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No {category} service with id {service_id} found!"
        )

    return service
