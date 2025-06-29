from fastapi import APIRouter, Path, status, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from typing import List, Annotated, Union
from sqlalchemy.orm import Session
import os

from schemas import resume_schemas
from cruds import resume_cruds
from database import db_session

router = APIRouter(
    prefix='/resumes',
    tags=['Resume']
)

# Directory to store uploaded resumes
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

RESUME_PATH = os.path.join(UPLOAD_DIR, "resume.pdf")

@router.get('/', response_model=List[resume_schemas.ResumeResponse], status_code=status.HTTP_200_OK)
async def get_resumes(
    db: db_session, 
    offset: Union[int, None] = 0, 
    limit: Union[Annotated[int, Path(le=10)], None] = 10
):
    resumes = resume_cruds.get_resumes(db, offset, limit)
    return resumes
    

@router.get('/{resume_id}', response_model=resume_schemas.ResumeResponse, status_code=status.HTTP_200_OK)
async def get_resume_by_id(db: db_session, resume_id: Annotated[int, Path(gt=0)]):
    resume = resume_cruds.get_resume_by_id(db, resume_id)
    return resume


@router.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    with open(RESUME_PATH, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"message": "Resume uploaded successfully."}

# Download route
@router.get("/download-resume/")
async def download_resume():
    if not os.path.exists(RESUME_PATH):
        raise HTTPException(status_code=404, detail="Resume not found.")
    return FileResponse(RESUME_PATH, media_type="application/pdf", filename="resume.pdf")