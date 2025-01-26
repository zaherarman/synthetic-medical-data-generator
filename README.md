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

## **Future Steps**
To make the synthetic data generator more realistic, consider implementing the following enhancements:

### 1. **Advanced Statistical Distributions**
- Use truncated normal, log-normal, or Poisson distributions for vitals, admissions, and counts.
- Add seasonality (e.g., flu admissions peak in winter) and trends to reflect real-world patterns.

### 2. **Correlations and Dependencies**
- Model realistic correlations (e.g., older patients → chronic conditions).
- Create conditional relationships (e.g., diagnoses → medications, severity → length of stay).

### 3. **Temporal Realism**
- Add time-series data for vitals and treatments (e.g., vitals fluctuate during admission).
- Ensure logical event sequences (e.g., admission → procedures → discharge).

### 4. **Domain-Specific Features**
- Include realistic medical standards (e.g., ICD-10 codes, lab result ranges).
- Expand datasets with lab tests, medications, and procedures.

### 5. **Handling Missing and Noisy Data**
- Simulate missingness patterns (e.g., MNAR, MCAR).
- Add noise to mimic real-world inconsistencies in data entry.

### Acknowledgements

Inspiration for project and metadata from:
- https://github.com/insightsengineering/random.cdisc.data/tree/main/R
- https://geminimedicine.ca/wp-content/uploads/2023/11/GEMINI_Data_Repository_Data_Dictionary_v4.0.0.html

