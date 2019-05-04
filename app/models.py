from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin
 
engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)

class DBSession():
  def __enter__(self):
    self.session = Session()
    return self.session

  def __exit__(self, exc_type, exc_value, traceback):
    self.session.close()

class User(Base, UserMixin):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  email = Column(String(64), nullable=False)
  username = Column(String(64), nullable=False)
  password = Column(String(64), nullable=False)
  zap_token = Column(String(64), nullable=False)

  def __repr__(self):
    return "<User id={}, username={}, email={}>".format(self.id, self.username, self.email)

class Update(Base):
  __tablename__ = 'updates'

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, nullable=False)
  percentage = Column(Integer, nullable=False)
  charging = Column(Integer, nullable=False)
  updated_at = Column(String(64), nullable=False)

  def __repr__(self):
    return "<Update id={}, user_id={}, percentage={}, charging={}, updated_at={}>".format(
      self.id, self.user_id, self.percentage, self.charging, self.updated_at)

  def toDict(self):
    valid_keys = ["id", "user_id", "percentage", "charging", "updated_at"]
    return {k:v for k,v in self.__dict__.items() if k in valid_keys}



