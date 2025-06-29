from datetime import datetime, date
from sqlalchemy import Column, Integer, Boolean, String, Text, Date, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from schemas import contact_schemas

Base = declarative_base()

# -------------------------
# SQLAlchemy ORM Models
# -------------------------

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True, index=True)
    imageNumber = Column(Boolean)
    title = Column(String(255), nullable=False)
    category = Column(String(100))
    link = Column(Text)
    image_link = Column(Text)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_date = Column(Date, nullable=True, default=None)
    created_by = Column(Integer, nullable=True, default=None)
    updated_by = Column(Integer, nullable=True, default=None)


class Service(Base):
    __tablename__ = 'services'
    
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(100))
    icon = Column(String(100))
    title = Column(String(255), nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_date = Column(Date, nullable=True, default=None)
    created_by = Column(Integer, nullable=True, default=None)
    updated_by = Column(Integer, nullable=True, default=None)


class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, index=True)
    published_at = Column(DateTime, default=datetime.utcnow)
    link = Column(Text)
    author = Column(String(100))
    title = Column(String(255))
    description = Column(Text)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_date = Column(Date, nullable=True, default=None)
    created_by = Column(Integer, nullable=True, default=None)
    updated_by = Column(Integer, nullable=True, default=None)


class Resume(Base):
    __tablename__ = 'resumes'
    
    id = Column(Integer, primary_key=True, index=True)
    start_year = Column(String(15))
    completion_year = Column(String(15))
    title = Column(String(255), nullable=False)
    school = Column(String(255))
    description = Column(Text)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_date = Column(Date, nullable=True, default=None)
    created_by = Column(Integer, nullable=True, default=None)
    updated_by = Column(Integer, nullable=True, default=None)


class Skill(Base):
    __tablename__ = 'skills'
    
    id = Column(Integer, primary_key=True, index=True)
    icon_class = Column(String(100))
    title = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_date = Column(Date, nullable=True, default=None)
    created_by = Column(Integer, nullable=True, default=None)
    updated_by = Column(Integer, nullable=True, default=None)


class Interest(Base):
    __tablename__ = 'interests'
    
    id = Column(Integer, primary_key=True, index=True)
    icon_class = Column(String(100))
    title = Column(String(100), nullable=False)
    description = Column(Text)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_date = Column(Date, nullable=True, default=None)
    created_by = Column(Integer, nullable=True, default=None)
    updated_by = Column(Integer, nullable=True, default=None)


class Contact(Base):
    __tablename__ = 'contacts'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150))
    message = Column(Text)
    status = Column(
        Enum(contact_schemas.MessageStatus), 
        default="pending",
        nullable=False
    )
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    # created_date = Column(Date, default=datetime.utcnow)
    updated_date = Column(Date, nullable=True, default=None)
    created_by = Column(Integer, nullable=True, default=None)
    updated_by = Column(Integer, nullable=True, default=None)
