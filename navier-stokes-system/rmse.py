import numpy as np

def compute_and_report_rmse(daily_indices, u_phys, v_phys, th_phys, m_phys, observed_data):
    u_err2, v_err2, th_err2, m_err2 = [], [], [], []
    
    for loop_idx, idx in enumerate(daily_indices):
        obs_idx = loop_idx
        obs_day = observed_data[obs_idx]
        
        u_err2.append((u_phys[idx] - obs_day["u_act"]) ** 2)
        v_err2.append((v_phys[idx] - obs_day["v_act"]) ** 2)
        th_err2.append((th_phys[idx] - obs_day["temp"]) ** 2)
        m_err2.append((m_phys[idx] - obs_day["pressure"]) ** 2)
        
    rmse_u = np.sqrt(np.mean(u_err2))
    rmse_v = np.sqrt(np.mean(v_err2))
    rmse_th = np.sqrt(np.mean(th_err2))
    rmse_m = np.sqrt(np.mean(m_err2))
    
    print("----------------------------------------------------")
    print("STATISTICAL VALIDATION & ERROR METRICS (RMSE)")
    print(f"U-Wind Speed RMSE : {rmse_u:.4f} m/s")
    print(f"V-Wind Speed RMSE : {rmse_v:.4f} m/s")
    print(f"Temperature RMSE  : {rmse_th:.4f} °C")
    print(f"Pressure RMSE     : {rmse_m:.4f} hPa")
    print("----------------------------------------------------")
    return rmse_u, rmse_v, rmse_th, rmse_m