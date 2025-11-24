from sqlalchemy import String,Integer, Column
from app.database import Base


class User(Base):
    __tablename__= "users"

    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)


