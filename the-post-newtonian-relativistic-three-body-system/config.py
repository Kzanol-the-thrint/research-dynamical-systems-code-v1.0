import os
import csv

# Engine Execution Parameters
DT = 300              # Temporal integration step size in seconds (5 minutes)
DAYS = 36500.0          # Forecast horizon in days
C_LIGHT = 2.99792458e8 # Speed of light in vacuum (m/s)
INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "output_1pn_data.csv"

def load_system_data(csv_path=INPUT_FILE):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Required data file '{csv_path}' was not found.")
        
    data = {}
    with open(csv_path, mode='r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row and len(row) >= 2:
                data[row[0].strip()] = float(row[1].strip())
                
    return data