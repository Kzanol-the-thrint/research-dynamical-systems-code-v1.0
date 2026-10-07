import csv
from datetime import datetime
import numpy as np

def load_observational_data(N, filepath, start_date_str, target_days=30):
    """
    Decoupled Ingestion Layer for SDCMS.
    Ingests and decomposes weather parameters into true vector components blowing TO.
    """
    try:
        target_start = datetime.strptime(start_date_str, "%d-%m-%Y")
    except ValueError:
        target_start = datetime.strptime(start_date_str, "%d/%m/%Y")
        
    dates = []
    observed_data = []
    start_index = None
    
    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames:
            reader.fieldnames = [field.strip().lower() for field in reader.fieldnames if field]
            
        all_rows = list(reader)
        
        for idx, row in enumerate(all_rows):
            raw_date = row.get('date', '').strip()
            if not raw_date:
                continue
            try:
                dt_obj = datetime.strptime(raw_date, "%d-%m-%Y")
            except ValueError:
                try:
                    dt_obj = datetime.strptime(raw_date, "%d/%m/%Y")
                except ValueError:
                    continue
            
            dates.append(dt_obj)
            ws = float(row.get('wind_speed', 0.0))
            wd = float(row.get('wind_dir', 0.0))
            temp = float(row.get('temp', 0.0))
            pressure = float(row.get('pressure', 0.0))
            
            rad = np.radians(wd)
            u_act = -ws * np.sin(rad)
            v_act = -ws * np.cos(rad)
            
            observed_data.append({
                "date": dt_obj.strftime("%d-%m-%Y"),
                "ws": ws, "wd": wd, "temp": temp, "pressure": pressure,
                "u_act": u_act, "v_act": v_act
            })
            
            if start_index is None and dt_obj >= target_start:
                start_index = len(observed_data) - 1

    if start_index is None:
        start_index = 0

    selected_obs = []
    target_dates = []
    for i in range(target_days):
        curr_idx = (start_index + i) % len(observed_data)
        selected_obs.append(observed_data[curr_idx])
        target_dates.append(observed_data[curr_idx]["date"])

    day0 = selected_obs[0]
    spatial_index = np.arange(N, dtype=np.int64)
    day0_obs = {
        "u": day0["u_act"] + ((spatial_index % 5) - 2) * 0.5,
        "v": day0["v_act"] + ((spatial_index % 3) - 1) * 0.5,
        "th": day0["temp"] + ((spatial_index % 4) - 2) * 0.2,
        "m": day0["pressure"] + ((spatial_index % 6) - 3) * 1.0
    }
    
    return day0_obs, selected_obs, target_dates