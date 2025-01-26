import random
import string
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from .data_models import Patient, Admission, Vitals, Transfusion
from .config import (HOSPITALS, 
                     COMMON_DIAGNOSES, 
                     HOSPITAL_SPECIALTIES, 
                     ADMISSION_LENGTH_POISSON_LAMBDA, 
                     TEMPERATURE_MEAN, TEMPERATURE_STDDEV, 
                     HEART_RATE_MEAN, 
                     HEART_RATE_STDDEV)

def _random_string(length=5):

    """Helper function to generate a random string."""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_patient_data(num_patients=25):

    patients = []

    for i in range(num_patients):
        pid = _random_string() 
        first_name = random.choice(["Arman", "Jane", "Alex", "Sara", "Mike", "Linda"])
        last_name = random.choice(["Zaher", "Johnson", "Williams", "Brown", "Jones"])
        
        # Random birth date between 1950-01-01 and 2025-01-01
        birth_timestamp = random.randint(int(datetime(1950, 1, 1).timestamp()), int(datetime(2025, 1, 1).timestamp()))
        birth_date = datetime.fromtimestamp(birth_timestamp).date()
        
        gender = random.choice(["M", "F", "Other"])
        race = random.choice(["White", "Black", "Asian", "South Asian", "Hispanic", "Extraterrestrial"])
        address = f"{random.randint(1,9999)} Grove Street"
        city = random.choice(["Toronto", "Waterloo", "Scarborough", "Milton", "Newmarket"])
        postal_code = f"{random.choice(string.ascii_uppercase)}{random.randint(0,9)}{random.choice(string.ascii_uppercase)} {random.randint(0,9)}{random.choice(string.ascii_uppercase)}{random.randint(0,9)}"

        patient = Patient(
            patient_id=pid,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            gender=gender,
            race=race,
            address=address,
            city=city,
            postal_code=postal_code
        )
        patients.append(patient)
    
    return patients

def generate_admissions_data(patients, avg_num_admissions=1):
    
    admissions = []
    admission_id_counter = 1
    
    for patient in patients:
        num_admissions = max(1, int(random.gauss(avg_num_admissions, 0.5)))
        
        for _ in range(num_admissions):
            admission_id = f"ADM-{admission_id_counter}"
            admission_id_counter += 1

            # Choose hospital
            hospital = random.choice(HOSPITALS)

            # Admission date in the last 3 years
            start_timestamp = random.randint(int((datetime.now() - timedelta(days=3*365)).timestamp()), int(datetime.now().timestamp()))
            admission_date = datetime.fromtimestamp(start_timestamp)
            
            # Use Poisson to get length of stay (ensuring at least 1 day)
            length_of_stay = max(1, np.random.poisson(lam=ADMISSION_LENGTH_POISSON_LAMBDA))
            discharge_date = admission_date + timedelta(days=length_of_stay)
            
            # Weighted primary diagnosis based on hospital specialty
            possible_diagnoses = COMMON_DIAGNOSES.copy()
            if hospital in HOSPITAL_SPECIALTIES:
                possible_diagnoses += HOSPITAL_SPECIALTIES[hospital] * 3  # weighting
            primary_diagnosis = random.choice(possible_diagnoses)
            
            # Random secondary diagnoses
            secondary_diagnoses = []
            if random.random() < 0.3:
                secondary_diagnoses.append(random.choice(COMMON_DIAGNOSES))
            
            admission = Admission(
                admission_id=admission_id,
                patient_id=patient.patient_id,
                hospital_name=hospital,
                admission_date=admission_date,
                discharge_date=discharge_date,
                primary_diagnosis=primary_diagnosis,
                secondary_diagnoses=secondary_diagnoses
            )
            admissions.append(admission)
    
    return admissions

def generate_vitals_data(admissions):
    vitals_records = []
    vitals_id_counter = 1
    
    for adm in admissions:
        num_days = (adm.discharge_date - adm.admission_date).days
        
        # 1-3 measurements each day
        for day in range(num_days):
            measurements_per_day = random.randint(1, 3)
            for i in range(measurements_per_day):
                measurement_time = adm.admission_date + timedelta(days=day, hours=random.randint(0, 23), minutes=random.randint(0, 59))
                vitals_id = f"VIT-{vitals_id_counter}"
                vitals_id_counter += 1
                
                # Temperature from a Normal distribution
                temperature_c = np.random.normal(loc=TEMPERATURE_MEAN, scale=TEMPERATURE_STDDEV)
                # Heart rate from a Normal distribution
                heart_rate = int(round(np.random.normal(loc=HEART_RATE_MEAN, scale=HEART_RATE_STDDEV)))
                
                # Blood pressure and respiratory rate can remain random or also be distributed
                bp_systolic = random.randint(100, 180)
                bp_diastolic = random.randint(60, 100)
                resp_rate = random.randint(12, 30)
                
                vitals_record = Vitals(
                    vitals_id=vitals_id,
                    patient_id=adm.patient_id,
                    admission_id=adm.admission_id,
                    measurement_time=measurement_time,
                    temperature_c=round(temperature_c, 1),  # round to 1 decimal
                    heart_rate=heart_rate,
                    blood_pressure_systolic=bp_systolic,
                    blood_pressure_diastolic=bp_diastolic,
                    respiratory_rate=resp_rate
                )
                vitals_records.append(vitals_record)
    return vitals_records

def generate_transfusion_data(admissions):
    
    transfusion_records = []
    transfusion_id_counter = 1
    blood_types = ["A", "B", "AB", "O"]
    
    for adm in admissions:

        # 15% chance
        if random.random() < 0.15:  

            # 1-3 transfusions during the stay
            num_transfusions = random.randint(1, 3)
            for _ in range(num_transfusions):
                transfusion_id = f"TRF-{transfusion_id_counter}"
                transfusion_id_counter += 1
                
                transfusion_date = adm.admission_date + timedelta(
                    days=random.randint(0, (adm.discharge_date - adm.admission_date).days),
                    hours=random.randint(0, 23)
                )
                blood_product_type = random.choice(blood_types)
                volume_ml = random.choice([250, 300, 500])
                
                transfusion_record = Transfusion(
                    transfusion_id=transfusion_id,
                    patient_id=adm.patient_id,
                    admission_id=adm.admission_id,
                    transfusion_date=transfusion_date,
                    blood_product_type=blood_product_type,
                    volume_ml=volume_ml
                )
                transfusion_records.append(transfusion_record)
    
    return transfusion_records
