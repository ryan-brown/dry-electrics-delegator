from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin
 
engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base(engine)

class Users(Base, UserMixin):
    __tablename__ = 'users'
 
    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    password = Column(String(64))
    zap_token = Column(String(64))

class Updates(Base, UserMixin):
    __tablename__ = 'updates'
 
    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    charging = Column(Integer)
    updated_at = Column(String(128))


def load_session():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

