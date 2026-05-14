from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase,Session
from app.config import settings
from typing import Annotated 
from fastapi import Depends

Database_url = settings.Database_url

engine = create_engine(Database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dep = Annotated[Session, Depends(get_db)]