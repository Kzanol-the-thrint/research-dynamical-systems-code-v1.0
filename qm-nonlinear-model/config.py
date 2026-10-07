import os
import csv

# Execution Parameters for Model #14 (Nonlinear Quantum Dynamics)
DT = 0.005          # Temporal step size
TOTAL_STEPS = 6000  # Number of simulation steps

# Physical Parameters for Gross-Pitaevskii / Nonlinear Schrödinger Model
# Representing quantum field amplitude evolution with self-interaction
MASS_Q = 1.0        # Effective particle mass
HBAR = 1.0          # Reduced Planck constant (normalized units)
POTENTIAL_V0 = 0.5  # External trapping potential strength
NONLINEAR_G = 1.2   # Self-interaction coupling constant (g > 0 for repulsion/stability)

INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "output_data.csv"

def load_system_data(csv_path=INPUT_FILE):
    if not os.path.exists(csv_path):
        return {
            "psi_real_init": 1.0,
            "psi_imag_init": 0.0
        }
        
    data = {}
    with open(csv_path, mode='r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row and len(row) >= 2:
                data[row[0].strip()] = float(row[1].strip())
    return data