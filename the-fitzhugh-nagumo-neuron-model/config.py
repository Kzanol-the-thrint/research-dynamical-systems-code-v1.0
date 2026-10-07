import os
import csv

DT = 0.05
HORIZON = 100.0
INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "output_fhn.csv"

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