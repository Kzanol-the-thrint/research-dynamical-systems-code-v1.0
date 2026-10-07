# config.py
import os
import csv

# Universal Engine Execution Parameters
DT = 0.1           # Lower temporal integration step size for smooth trajectories
HORIZON = 800       # Forecast horizon steps/time units
INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "output_data.csv"

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