from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import SessionLocal, engine, Base
from pydantic import BaseModel
from models import User, Log
import datetime as dt
import random as rd


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def get_database():
    db = None

    try:
        db = SessionLocal()
    finally:
        yield db
        db.close()

    
class UserModel(BaseModel):
    username: str
    password: str
    email: str


class RegisterModel(BaseModel):
    username: str
    password: str
    confirm: str
    first_name: str
    last_name: str
    contact: str
    email: str


class LogModel(BaseModel):
    turbidity: int
    humidity: int
    tds: int
    ec: int
    user_id: int



@app.post('/login')
async def login(username: str, password: str, db: Session = Depends(get_database)):
    try:
        existing_user = db.query(User).filter(User.username == username).first()

        if existing_user:
            if existing_user.password == password:
                return { 'response': 'Login successful.', 'user_data': existing_user, 'status_code': 200 }
            else:
                return { 'response': 'Login failed.', 'status_code': 403 }
    except:
        return { 'response': 'Login failed.', 'status_code': 403 }


@app.post('/register')
async def register(user: RegisterModel, db: Session = Depends(get_database)):
    try:
        existing_user = db.query(User).filter(User.username == user.username).first()

        if not existing_user:
            if user.password == user.confirm:
                new_user = User()
                new_user.username = user.username
                new_user.password = user.password
                new_user.first_name = user.first_name
                new_user.last_name = user.last_name
                new_user.contact = user.contact
                new_user.email = user.email

                db.add(new_user)
                db.commit()

                return { 'response': 'Registration successful.', 'status_code': 200 }
        else:
            return { 'response': 'User already exists.', 'status_code': 403 }
    except:
        return { 'response': 'Registration failed.', 'status_code': 400 }


@app.post('/insert_entry')
async def insert_log(log: LogModel, db: Session = Depends(get_database)):
    try:
        new_entry = Log()
        new_entry.turbidity = log.turbidity
        new_entry.ph = log.humidity 
        new_entry.tds = log.tds
        new_entry.date_created = dt.datetime.now()
        new_entry.record_owner = log.user_id

        db.add(new_entry)
        db.commit()
        
        return { 'response': 'Log added.', 'status_code': 200 }
    except:
        return { 'response': 'Failed to add log.', 'status_code': 403 }


@app.get('/retrieve_dashboard_data')
async def retrieve_dashboard_data(user_id: int, db: Session = Depends(get_database)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        average_turbidity = db.query(func.avg(Log.turbidity)).filter(Log.record_owner == user_id).scalar()
        average_ph = db.query(func.avg(Log.ph)).filter(Log.record_owner == user_id).scalar()
        average_tds = db.query(func.avg(Log.tds)).filter(Log.record_owner == user_id).scalar()
        average_ec = db.query(func.avg(Log.ec)).filter(Log.record_owner == user_id).scalar()

        payload = {}
        payload.update({ 'user_data': user })
        payload.update({ 'avg_turbidity': average_turbidity })
        payload.update({ 'average_ph': average_ph })
        payload.update({ 'average_tds': average_tds })
        payload.update({ 'average_ec': average_ec })

        return { 'payload': payload, 'status_code': 200 }
    except:
        return { 'response': 'Error retrieving data.', 'status_code': 400 }


@app.get('/all_entries')
async def retrieve_entries(user_id: int, db: Session = Depends(get_database)):
    try:
        entries = db.query(Log).filter(Log.record_owner == user_id).all()

        return { 'payload': entries, 'status_code': 200 }
    except:
        return { 'response': 'Error retrieving data.', 'status_code': 400 }
    

@app.get('/generate_dummy')
async def generate_dummy(db: Session = Depends(get_database)):
    try:
        for x in range(20):
            new_entry = Log()

            new_entry.ph = rd.randint(10, 20)
            new_entry.turbidity = rd.randint(10, 20)
            new_entry.tds = rd.randint(10, 20)
            new_entry.ec = rd.randint(10, 20)
            new_entry.record_owner = 1

            db.add(new_entry)
            db.commit()

        return { 'response': 'Generation completed.', 'status_code': 200 }
    except:
        return { 'response': 'Generation Failed.', 'status_code': 400 }