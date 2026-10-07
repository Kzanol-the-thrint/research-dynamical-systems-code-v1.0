# config.py
import os
import csv

# Engine Execution Parameters for Lorenz Model
DT = 0.005          # Temporal integration step size (delta_t)
DAYS = 400          # Total forecast duration in simulation time units
INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "lorenz_output_data.csv"

def load_system_data(csv_path=INPUT_FILE):
    """
    Loads raw Lorenz system metrics and parameters directly from CSV.
    """
    if not os.path.exists(csv_path):
        csv_path = "input_data.csv"
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required data file was not found.")
        
    data = {}
    with open(csv_path, mode='r') as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header row
        for row in reader:
            if row and len(row) >= 2:
                data[row[0].strip()] = float(row[1].strip())
                
    return data