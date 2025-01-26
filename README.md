# Synthetic Medical Data Generator

A Python package for generating realistic synthetic healthcare data for testing, development, and demonstration purposes. The package supports generating various datasets like patient demographics, hospital admissions, vitals, and transfusions, with logical consistency and probabilistic relationships.

## **Features**

- Generate synthetic data for:
  - **Patients**: Demographics such as age, gender, race, and address.
  - **Hospital Admissions**: Admission and discharge dates, diagnoses, and hospital information.
  - **Vitals**: Temperature, heart rate, blood pressure, and more using realistic distributions.
  - **Transfusions**: Blood product details and volumes.
- Logical consistency:
  - Discharge dates are always after admission dates.
  - Weighted diagnoses based on hospital specialties.
- Advanced distributions:
  - Poisson distribution for length of stay.
  - Normal distribution for vitals (e.g., temperature, heart rate).
- Export datasets to CSV, JSON, or Excel.
- Built-in data validation using Pydantic schemas.
- Extensible and modular design for additional data types.

## Inspiration

- https://github.com/insightsengineering/random.cdisc.data/tree/main/R
- https://geminimedicine.ca/wp-content/uploads/2023/11/GEMINI_Data_Repository_Data_Dictionary_v4.0.0.html

