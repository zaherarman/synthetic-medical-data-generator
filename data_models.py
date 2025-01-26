from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

class Patient(BaseModel):
    patient_id: str
    first_name: str
    last_name: str
    birth_date: date
    gender: str
    race: Optional[str]
    address: Optional[str]
    city: Optional[str]
    postal_code: Optional[str]

class Admission(BaseModel):
    admission_id: str
    patient_id: str
    hospital_name: str
    admission_date: datetime
    discharge_date: datetime
    primary_diagnosis: Optional[str]
    secondary_diagnoses: Optional[List[str]]

class Vitals(BaseModel):
    vitals_id: str
    patient_id: str
    admission_id: str
    measurement_time: datetime
    temperature_c: float
    heart_rate: int
    blood_pressure_systolic: int
    blood_pressure_diastolic: int
    respiratory_rate: int

class Transfusion(BaseModel):
    transfusion_id: str
    patient_id: str
    admission_id: str
    transfusion_date: datetime
    blood_product_type: str
    volume_ml: float

# Possible additions: Pharmacy, Lab, Radiology
# date: YYYY-MM-DD, datetime: YYYY-MM-DDTHH:MM:SS

