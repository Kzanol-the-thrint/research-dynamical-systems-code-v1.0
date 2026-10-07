import os
import csv

# Execution Parameters for the Combined TOE / GUT Conjugate Model
DT = 0.005          # Temporal step size
TOTAL_STEPS = 8000  # Number of simulation steps

# Unified Coupling Parameters
C_LIGHT = 2.9979e8  
G_CONST = 6.6743e-11
COUPLING_LAMBDA = 0.5  # Bridge coupling constant linking GR and QM sectors

INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "output_data.csv"

def load_system_data(csv_path=INPUT_FILE):
    if not os.path.exists(csv_path):
        return {
            "psi_gr_init": 1.0,
            "p_gr_init": 0.05,
            "psi_qm_real_init": 1.0,
            "psi_qm_imag_init": 0.2
        }
        
    data = {}
    with open(csv_path, mode='r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row and len(row) >= 2:
                data[row[0].strip()] = float(row[1].strip())
    return data