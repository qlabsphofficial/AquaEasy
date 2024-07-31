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
    deleted_log_records = relationship('DeletedLog', back_populates='deleted_record_owner')


class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, autoincrement=True, primary_key=True)
    turbidity = Column(Float)
    ph = Column(Float)
    tds = Column(Float)
    ec = Column(Float)
    battery = Column(Float)
    turbidity_remark = Column(String)
    ph_remark = Column(String)
    tds_remark = Column(String)
    ec_remark = Column(String)
    date_created = Column(DateTime, server_default=func.now())
    record_owner = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='log_records')


class DeletedLog(Base):
    __tablename__ = 'deleted_logs'

    id = Column(Integer, autoincrement=True, primary_key=True)
    turbidity = Column(Float)
    ph = Column(Float)
    tds = Column(Float)
    ec = Column(Float)
    battery = Column(Float)
    turbidity_remark = Column(String)
    ph_remark = Column(String)
    tds_remark = Column(String)
    ec_remark = Column(String)
    date_created_log = Column(DateTime, server_default=func.now())
    date_deleted = Column(DateTime, server_default=func.now())
    record_owner = Column(Integer, ForeignKey('users.id'))

    deleted_record_owner = relationship('User', back_populates='deleted_log_records')