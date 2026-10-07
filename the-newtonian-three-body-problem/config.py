# config.py
import os
import csv

# Engine Execution Parameters
DT = 300              # Temporal integration step size in seconds (300.0 = 5 minutes)
DAYS = 36500.0          # Forecast horizon in days
INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "output_data.csv"

def load_system_data(csv_path=INPUT_FILE):
    """Loads raw system metrics directly from CSV."""
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