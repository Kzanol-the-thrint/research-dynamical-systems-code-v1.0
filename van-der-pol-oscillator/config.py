import os
import csv

# Universal Engine Execution Parameters
DT = 0.05             # Temporal integration step size for smooth limit-cycle tracking
HORIZON = 40.0        # Forecast horizon time units
INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "output_data.csv"

def load_system_data(csv_path=INPUT_FILE):
    """
    Loads universal system parameters and initial state vectors from CSV.
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