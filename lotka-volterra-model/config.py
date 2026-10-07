# config.py
import os
import csv

# Engine Execution Parameters
DT = 0.01             # Temporal integration step size (fractional time units)
TIME_HORIZON = 50.0   # Forecast horizon length
INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "output_lv_trajectory.csv"

def load_system_data(csv_path=INPUT_FILE):
    """
    Loads raw ecological parameters and initial state metrics from CSV.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Required data file '{csv_path}' was not found.")
        
    data = {}
    with open(csv_path, mode='r') as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header row
        for row in reader:
            if row and len(row) >= 2:
                data[row[0].strip()] = float(row[1].strip())
                
    return data