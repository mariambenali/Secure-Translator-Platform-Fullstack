from fastapi import FastAPI ,Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, get_db
from app.schema import UserResponse, UserCreate
from app.models import User


app= FastAPI()


@app.post("/register", response_model=UserResponse)
def create_user(user:UserCreate, db:Session= Depends(get_db)):
    new_user=User(username=user.username,
                  password=user.password,
                  email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh()
    return new_user

