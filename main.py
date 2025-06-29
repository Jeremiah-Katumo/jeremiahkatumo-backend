
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import models
from database import engine
from routes import skill_routes, interest_routes, contact_routes, resume_routes


app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Welcome to Jeremiah Katumo"}   


app.include_router(skill_routes.router)
app.include_router(interest_routes.router)
app.include_router(contact_routes.router)
app.include_router(resume_routes.router)