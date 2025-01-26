import os
from synthetic_data_generator.data_generators import (
    generate_patient_data,
    generate_admissions_data,
    generate_vitals_data,
    generate_transfusion_data,
)
from synthetic_data_generator.utils import export_data

# Generate data
patients = generate_patient_data(num_patients=10)
admissions = generate_admissions_data(patients, avg_num_admissions=2)
vitals = generate_vitals_data(admissions)
transfusions = generate_transfusion_data(admissions)

# Export data to CSV in a visible folder
output_folder = "synthetic_output"
os.makedirs(output_folder, exist_ok=True)

export_data(patients, os.path.join(output_folder, "patients.csv"))
export_data(admissions, os.path.join(output_folder, "admissions.csv"))
export_data(vitals, os.path.join(output_folder, "vitals.csv"))
export_data(transfusions, os.path.join(output_folder, "transfusions.csv"))

print(f"Data has been exported to the {output_folder}/ folder.")
