from fastapi import FastAPI ,Depends, HTTPException, Header
from sqlalchemy.orm import Session
from fastapi.concurrency import run_in_threadpool
from app.database import SessionLocal, engine, get_db, Base
from app.schema import UserResponse, UserCreate, Login, Translate
from app.config import SECRET_KEY, ALGORITHM, HF_TOKEN
from app.models import User
from app.translator import translate_text
from jose import jwt




app= FastAPI()
Base.metadata.create_all(bind=engine)


@app.post("/register", response_model=UserResponse)
def create_user(user:UserCreate, db:Session= Depends(get_db)):
    new_user=User(username=user.username,
                  password=user.password,
                  email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login")
def login(data: Login, db:Session=Depends(get_db)):
    user= db.query(User).filter(User.username == data.username).first()
    if not User:
        return {"Error":"Not found!"}
    elif user.password != data.password:
        return {"Error":"Password invalid!"}

    payload={"username":data.username}
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

    return {"Message" : "Logged successfully. Welcome!",
            "token" :token}


@app.post("/translate")
async def translation(payload: Translate, current_user: dict = Depends(login)):
    result = await run_in_threadpool(
        translate_text,
        payload.text,
        payload.source,
        payload.target
    )
    return {"translated": result}