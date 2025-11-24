from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os


load_dotenv()

#import variables from .env
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")

#import url database .env
DATABASE_URL=os.getenv("DATABASE")

#create engine
engine=create_engine(DATABASE_URL)

#create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base= declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
