import os
import csv

# Schwarzschild Relativistic Orbital Engine Execution Parameters
DT = 1.0                  # Integration step size in seconds
HORIZON_STEPS = 10000     # Total integration steps
G_CONST = 6.67430e-11     # Newtonian Gravitational Constant (m^3 kg^-1 s^-2)
M_CENTRAL = 1.989e30      # Central Mass (Solar Masses in kg)
C_LIGHT = 2.99792458e8    # Speed of Light in m/s

INPUT_FILE = "input_orbital.csv"
OUTPUT_FILE = "output_schwarzschild_data.csv"

def load_system_data(csv_path=INPUT_FILE):
    """
    Ingests initial orbital conditions for relativistic Schwarzschild motion.
    State vector: [r, phi, r_dot, phi_dot]
    """
    if not os.path.exists(csv_path):
        return {
            "r_init": 1.5e11,       # ~1 AU initial radial distance (m)
            "phi_init": 0.0,        # Initial angular position (rad)
            "r_dot_init": 0.0,      # Radial velocity (m/s)
            "phi_dot_init": 1.99e-7 # Orbital angular velocity (rad/s)
        }
        
    data = {}
    with open(csv_path, mode='r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row and len(row) >= 2:
                data[row[0].strip()] = float(row[1].strip())
    return data