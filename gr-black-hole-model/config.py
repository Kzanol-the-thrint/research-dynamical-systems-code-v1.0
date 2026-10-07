import os
import csv

# Curve-Optimized Engine Parameters for Model #13
# Natural oscillation period for r = 150,000m is ~387,992 seconds.
# We set DT = 200 seconds and TOTAL_STEPS = 8000 to capture ~4 full oscillation cycles 
# guaranteeing complete, looping elliptical phase-space curves!
DT = 200.0          
TOTAL_STEPS = 8000  
C_LIGHT = 2.99792458e8  
G_CONST = 6.6743e-11
BH_MASS = 2.0e30    # Solar mass black hole
MULTIPOLE_L = 2     # Quadrupole mode

INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "output_data.csv"

def load_system_data(csv_path=INPUT_FILE):
    if not os.path.exists(csv_path):
        return {
            "psi_init": 1.0,
            "p_init": 0.05,     # Non-zero initial momentum gives the ellipse an immediate transverse kick!
            "r_radius": 1.5e5   # Radial distance from event horizon
        }
        
    data = {}
    with open(csv_path, mode='r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row and len(row) >= 2:
                data[row[0].strip()] = float(row[1].strip())
    return data