from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import SessionLocal, engine, Base
from pydantic import BaseModel
from models import User, Log, DeletedLog
import datetime as dt
import random as rd
from sqladmin import Admin, ModelView

app = FastAPI()
admin = Admin(app, engine)

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
    turbidity: float
    humidity: float
    tds: float
    ec: float
    battery: float
    user_id: int


class UserAdminModel(ModelView, model=User):
    column_list = [User.id, User.username, User.password, User.first_name, User.last_name, User.contact, User.email]


class LogAdminModel(ModelView, model=Log):
    column_list = [Log.id, Log.turbidity, Log.ph, Log.tds, Log.ec, Log.battery, Log.date_created, Log.record_owner]


class DeletedLogAdminModel(ModelView, model=DeletedLog):
    column_list = [
        DeletedLog.id, 
        DeletedLog.turbidity, 
        DeletedLog.ph, 
        DeletedLog.tds, 
        DeletedLog.ec, 
        DeletedLog.battery, 
        DeletedLog.date_created_log, 
        DeletedLog.date_deleted,
        DeletedLog.record_owner
    ]


admin.add_view(UserAdminModel)
admin.add_view(LogAdminModel)
admin.add_view(DeletedLogAdminModel)


@app.get('/show_users')
async def show_users(db: Session = Depends(get_database)):
    try:
        all_users = db.query(User).all()
        return { 'response': 'User Retrieval Success', 'users': all_users, 'status_code': 200 }
    except:
        return { 'response': 'User Retrieval Failed', 'status_code': 200 }


# @app.get('/retrieve_logs')
# async def retrieve_logs(db: Session = Depends(get_database)):
#     try:
#         all_logs = db.query(Log).all()
#         return { 'response': 'Log Retrieval Success', 'logs': all_logs, 'status_code': 200 }
#     except:
#         return { 'response': 'Log Retrieval Failed', 'status_code': 200 }


# @app.get('/retrieve_deleted_logs')
# async def retrieve_deleted_logs(db: Session = Depends(get_database)):
#     try:
#         all_deleted_logs = db.query(DeletedLog).all()
#         return { 'response': 'Deleted Log Retrieval Success', 'deleted_logs': all_deleted_logs, 'status_code': 200 }
#     except:
#         return { 'response': 'Deleted Log Retrieval Failed', 'status_code': 200 }
    

@app.get('/retrieve_user_data')
async def retrieve_user_data(user_id: int, db: Session = Depends(get_database)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        return { 'response': 'User Retrieval Success', 'user': user, 'status_code': 200 }
    except:
        return { 'response': 'User Retrieval Failed', 'status_code': 200 }


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

                return { 'response': 'Registration successful.', 'status_code': 200, 'new_user_id': new_user.id }
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
        new_entry.ec = log.ec
        new_entry.battery = log.battery
        new_entry.date_created = dt.datetime.now()
        new_entry.record_owner = log.user_id

        db.add(new_entry)
        db.commit()
        
        return { 'response': 'Log added.', 'status_code': 200 }
    except:
        return { 'response': 'Failed to add log.', 'status_code': 403 }


# @app.post('/insert_deleted_entry')
# async def insert_deleted_log(log: LogModel, db: Session = Depends(get_database)):
#     try:
#         new_entry = DeletedLog()
#         new_entry.turbidity = log.turbidity
#         new_entry.ph = log.humidity 
#         new_entry.tds = log.tds
#         new_entry.ec = log.ec
#         new_entry.battery = log.battery
#         new_entry.date_created = dt.datetime.now()
#         new_entry.record_owner = log.user_id

#         db.add(new_entry)
#         db.commit()
        
#         return { 'response': 'Deleted Log added.', 'status_code': 200 }
#     except:
#         return { 'response': 'Deleted Failed to add log.', 'status_code': 403 }


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


@app.get('/all_deleted_entries')
async def retrieve_deleted_entries(user_id: int, db: Session = Depends(get_database)):
    try:
        entries = db.query(DeletedLog).filter(DeletedLog.record_owner == user_id).all()

        return { 'payload': entries, 'status_code': 200 }
    except:
        return { 'response': 'Error retrieving data.', 'status_code': 400 }


@app.get('/delete_entry')
async def delete_entry(entry_id: int, db: Session = Depends(get_database)):
    # try:
        entry = db.query(Log).filter(Log.id == entry_id).first()

        if entry:
            deleted_entry = DeletedLog()
            deleted_entry.turbidity = entry.turbidity
            deleted_entry.ph = entry.ph
            deleted_entry.tds = entry.tds
            deleted_entry.ec = entry.ec
            deleted_entry.battery = entry.battery
            deleted_entry.date_created_log = entry.date_created
            deleted_entry.record_owner = entry.record_owner

            db.add(deleted_entry)
            db.delete(entry)
            db.commit()

        print('testing')
        return { 'response': 'Data Deleted', 'status_code': 200 }
    # except:
    #     print('hi')
    #     return { 'response': 'Error deleting data.', 'status_code': 400 }
    

# @app.get('/delete_user')
# async def delete_user(user_id: int, db: Session = Depends(get_database)):
#     try:
#         entry = db.query(User).filter(User.id == user_id).first()

#         if entry:
#             db.delete(entry)
#             db.commit()

#         return { 'response': 'Data Deleted', 'status_code': 200 }
#     except:
#         return { 'response': 'Error deleting data.', 'status_code': 400 }


# @app.get('/delete_logs')
# async def delete_logs(log_id: int, db: Session = Depends(get_database)):
#     try:
#         entry = db.query(Log).filter(Log.id == log_id).first()

#         if entry:
#             db.delete(entry)
#             db.commit()

#         return { 'response': 'Data Deleted', 'status_code': 200 }
#     except:
#         return { 'response': 'Error deleting data.', 'status_code': 400 }


# @app.get('/delete_deleted_logs')
# async def delete_deleted_logs(log_id: int, db: Session = Depends(get_database)):
#     try:
#         entry = db.query(DeletedLog).filter(DeletedLog.id == log_id).first()

#         if entry:
#             db.delete(entry)
#             db.commit()

#         return { 'response': 'Data Deleted', 'status_code': 200 }
#     except:
#         return { 'response': 'Error deleting data.', 'status_code': 400 }


# @app.get('/delete_all_users')
# async def delete_all_users(db: Session = Depends(get_database)):
#     try:
#         entries = db.query(User).all()
#         print(entries)

#         for entry in entries:
#             db.delete(entry)

#         db.commit()

#         return { 'response': 'User Deleted', 'status_code': 200 }
#     except:
#         return { 'response': 'Error deleting data.', 'status_code': 400 }


# @app.get('/delete_all_entries')
# async def delete_all_entries(db: Session = Depends(get_database)):
#     try:
#         entries = db.query(Log).all()
#         print(entries)

#         for entry in entries:
#             db.delete(entry)

#         db.commit()

#         return { 'response': 'Data Deleted', 'status_code': 200 }
#     except:
#         return { 'response': 'Error deleting data.', 'status_code': 400 }


# @app.get('/delete_all_deleted_entries')
# async def delete_all_deleted_entries(db: Session = Depends(get_database)):
#     try:
#         entries = db.query(DeletedLog).all()
#         print(entries)

#         for entry in entries:
#             db.delete(entry)

#         db.commit()

#         return { 'response': 'Data Deleted', 'status_code': 200 }
#     except:
#         return { 'response': 'Error deleting data.', 'status_code': 400 }


# @app.post('/update_user')
# async def update_user(user: RegisterModel, db: Session = Depends(get_database)):
#     # try:
#         existing_user = db.query(User).filter(User.id == user.).first()

#         if not existing_user:
#             new_resume = Resume()
#             new_resume.resume_owner = resume.resume_owner
#             new_resume.ed_1 = resume.ed_1
#             new_resume.ed_2 = resume.ed_2
#             new_resume.ed_3 = resume.ed_3
#             new_resume.summary = resume.summary
#             new_resume.ref_1 = resume.ref_1
#             new_resume.ref_2 = resume.ref_2
#             new_resume.ref_3 = resume.ref_3
#             db.add(new_resume)
#             db.commit()

#         else:
#             existing_user.username = resume.resume_owner
#             existing_user.password = resume.ed_1
#             existing_user.first_name = resume.ed_2
#             existing_user.last_name = resume.ed_3
#             existing_user.contact = resume.summary
#             existing_user.email = resume.ref_1
#             db.commit()

#         return { 'response': 'resume submitted', 'status_code': 200 }
#     # except:
#     #     return { 'response': 'Error retrieving data.', 'status_code': 400 }
    