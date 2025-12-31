from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class VitalSigns(Base):
    __tablename__ = "vital_signs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    heart_rate = Column(Float)
    spo2 = Column(Float)
    temperature = Column(Float)
    systolic_bp = Column(Integer)
    diastolic_bp = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    is_anomaly = Column(Boolean, default=False)
    anomaly_type = Column(String)
    confidence = Column(Float)

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    alert_type = Column(String)
    message = Column(String)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
