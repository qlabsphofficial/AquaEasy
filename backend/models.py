from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)

    log_records = relationship('Log', back_populates='owner')

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, autoincrement=True, primary_key=True)
    turbidity = Column(Float)
    humidity = Column(Float)
    tds = Column(Float)
    date_created = Column(DateTime)
    record_owner = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='log_records')