from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    contact = Column(String)
    email = Column(String)

    log_records = relationship('Log', back_populates='owner')

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, autoincrement=True, primary_key=True)
    turbidity = Column(Float)
    ph = Column(Float)
    tds = Column(Float)
    ec = Column(Float)
    battery = Column(Float)
    date_created = Column(DateTime, server_default=func.now())
    record_owner = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='log_records')