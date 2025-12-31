from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(100))
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    age = Column(Integer)
    gender = Column(String(10))
    weight = Column(Float)
    height = Column(Float)
    medical_history = Column(Text)
    emergency_contact = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

class VitalSigns(Base):
    __tablename__ = "vital_signs"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, index=True)
    heart_rate = Column(Float)  # BPM
    spo2 = Column(Float)        # Blood oxygen %
    temperature = Column(Float) # Celsius
    systolic_bp = Column(Integer)  # Blood pressure
    diastolic_bp = Column(Integer)
    respiratory_rate = Column(Float)
    glucose_level = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    is_anomaly = Column(Boolean, default=False)
    anomaly_type = Column(String(50))
    confidence = Column(Float)
    processed = Column(Boolean, default=False)

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, index=True)
    alert_type = Column(String(20))  # emergency/warning/info
    message = Column(String(500))
    severity = Column(String(20))  # high/medium/low
    is_read = Column(Boolean, default=False)
    is_resolved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    resolved_at = Column(DateTime, nullable=True)
    action_taken = Column(Text)

class PredictionLog(Base):
    __tablename__ = "prediction_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, index=True)
    input_data = Column(Text)  # JSON string of input
    prediction = Column(Text)  # JSON string of output
    processing_time = Column(Float)  # seconds
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
