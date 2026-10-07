import os
import csv
import numpy as np

def export_csv_results(output_dir, target_days, target_dates, observed_data, u_phys, v_phys, w_phys, th_phys, m_phys, steps):
    os.makedirs(output_dir, exist_ok=True)

    steps_per_day = steps // target_days if target_days > 0 else steps
    daily_indices = [day * steps_per_day for day in range(1, target_days + 1)]
    daily_indices[-1] = min(daily_indices[-1], steps - 1)

    param_config = [
        ("u_wind_speed", "Horizontal 1 U Wind Speed (m/s)", u_phys, "u"),
        ("v_wind_speed", "Horizontal 2 V Wind Speed (m/s)", v_phys, "v"),
        ("w_wind_speed", "Vertical W Wind Speed (m/s)", w_phys, "w"),
        ("temperature", "Temperature (°C)", th_phys, "th"),
        ("pressure", "Pressure (hPa)", m_phys, "m")
    ]

    exported_files = []
    for p_key, p_label, series, obs_key in param_config:
        rows = []
        for loop_idx, idx in enumerate(daily_indices):
            day_no = loop_idx + 1  
            obs_idx = loop_idx  
            
            date_str = target_dates[obs_idx] if obs_idx < len(target_dates) else f"Day {day_no}"
            pred_val = float(series[idx])
            
            if obs_idx < len(observed_data):
                if obs_key == "u":
                    act_val = observed_data[obs_idx]["u_act"]
                elif obs_key == "v":
                    act_val = observed_data[obs_idx]["v_act"]
                elif obs_key == "th":
                    act_val = observed_data[obs_idx]["temp"]
                elif obs_key == "m":
                    act_val = observed_data[obs_idx]["pressure"]
                else:
                    act_val = 0.0
            else:
                act_val = 0.0
                
            error = pred_val - act_val
            rows.append({
                "Day": day_no,
                "Date": date_str,
                "Predicted": round(pred_val, 4),
                "Actual": round(act_val, 4),
                "Error": round(error, 4)
            })

        filepath = os.path.join(output_dir, f"{p_key}_forecast.csv")
        with open(filepath, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["Day", "Date", "Predicted", "Actual", "Error"])
            writer.writeheader()
            writer.writerows(rows)
        exported_files.append(filepath)

    return exported_files, daily_indices, param_config