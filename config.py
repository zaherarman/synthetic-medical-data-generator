HOSPITALS = ["Grand River Hospital", 
             "Oakville Trafalgar Memorial Hospital", 
             "Hamilton General Hospital", 
             "Humber River Hospital", 
             "Kingston General Hospital", 
             "University Hospital", 
             "Sinai Health System", 
             "Greater Niagara General Site", 
             "Sunnybrook Health Sciences Centre", 
             "St. Michael's Hospital"]

COMMON_DIAGNOSES = ["Flu", 
                    "Pneumonia", 
                    "COPD", 
                    "Heart Failure", 
                    "Hypertension", 
                    "Diabetes"]

# Example of hospital specialities and probabilities
HOSPITAL_SPECIALTIES = { "Hamilton General Hospital": ["Heart Failure", "Hypertension"], 
                        "Sunnybrook Health Sciences Centre": ["Heart Failure", "COPD"], 
                        "St. Michael's Hospital": ["Diabetes", "Pneumonia"]}

# Probability distribution parameters

# Estimatting the average length-of-stay is 5 days (Poisson) with a lambda=5
ADMISSION_LENGTH_POISSON_LAMBDA = 5

# Normal distribution parameters for vitals
TEMPERATURE_MEAN = 36.8
TEMPERATURE_STDDEV = 0.4  

HEART_RATE_MEAN = 80
HEART_RATE_STDDEV = 15

# More advanced distribution paramters can be added for more realistic generatng