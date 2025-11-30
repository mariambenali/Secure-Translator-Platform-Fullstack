from fastapi import FastAPI ,Depends, HTTPException, Header
from sqlalchemy.orm import Session
from fastapi.concurrency import run_in_threadpool
from app.database import SessionLocal, engine, get_db, Base
from app.schema import UserResponse, UserCreate, Login, Translate
from app.config import SECRET_KEY, ALGORITHM, HF_TOKEN
from app.models import User
from app.translator import translate_text
from jose import jwt
from fastapi.middleware.cors import CORSMiddleware



app= FastAPI()
Base.metadata.create_all(bind=engine)

origins =["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins =origins,
    allow_credentials =True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    elif user.password != data.password:
        raise HTTPException(status_code=401, detail="Invalid password")

    payload={"username":data.username}
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return {"token" :token}

@app.get("/")
def get_token(token:str, str = Header()):
    try:
        decoded= jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decoded
    except Exception as e:
        raise HTTPException(status_code=401, detail="Verify Token")
    


@app.post("/translate")
def translation(payload: Translate, authorization: str = Header()):
    token = authorization.replace("Bearer ", "") 

    print("PAYLOAD ", payload)
    print("TOKEN ", token)

    result = translate_text(
        payload.text,
        payload.source,
        payload.target
    )
    return {"translated": result}

