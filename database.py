from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends
from dotenv import load_dotenv
import os

from utils.config import DATABASE_DRIVER, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME


# Load environment variables from .env file
load_dotenv()

# Get environment variables

DATABASE_DRIVER = DATABASE_DRIVER
DATABASE_USER = DATABASE_USER
DATABASE_PASSWORD = DATABASE_PASSWORD
DATABASE_HOST = DATABASE_HOST
DATABASE_PORT = DATABASE_PORT
DATABASE_NAME = DATABASE_NAME

pymysql.install_as_MySQLdb()

SQLALCHEMY_DATABASE_URL = f'{DATABASE_DRIVER}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_session = Annotated[Session, Depends(get_db)]