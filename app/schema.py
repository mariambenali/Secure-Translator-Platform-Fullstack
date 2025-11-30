from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    email: str


class UserResponse(BaseModel):
    id :int
    username: str
    email: str

    class Config:
        model_config = {
            "from_attributes": True
            }


class Login(BaseModel):
    username: str
    password: str


class Translate(BaseModel):
    text : str
    source: str
    target: str

