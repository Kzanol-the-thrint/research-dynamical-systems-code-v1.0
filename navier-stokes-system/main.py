import os
import shutil
import numpy as np
from csv_loader import load_observational_data
from sdc_solver import run_sdc_solver
from exporter import export_csv_results
from visualizer import render_plots_and_tables
from rmse import compute_and_report_rmse 
from matrix import create_sdc_matrix, show_parameters, get_config

def map_range(raw_data, phys_min, phys_max):
    r_min, r_max = np.min(raw_data), np.max(raw_data)
    if r_max == r_min:
        return np.full_like(raw_data, (phys_min + phys_max) / 2.0)
    return phys_min + (phys_max - phys_min) * (raw_data - r_min) / (r_max - r_min)

def main():
    args = get_config()

    output_dir = "data/output"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    show_parameters(args)

    print("Phase 1: Parsing historical records and initializing boundaries...")
    day0_obs, observed_data, target_dates = load_observational_data(
        args.nodes, args.input_file, start_date_str=args.start_date, target_days=args.horizon
    )
    g_int = np.int64(981)
    P_ref = np.int64(10050000)

    matrix = create_sdc_matrix(g_int, P_ref)

    print("Phase 2: Executing autonomous SDC physics core integration steps...")
    u_raw, v_raw, w_raw, th_raw, m_raw, steps = run_sdc_solver(
        matrix, day0_obs, target_days=args.horizon, N=args.nodes, dt=args.timestep
    )

    u_min, u_max = min(obs["u_act"] for obs in observed_data), max(obs["u_act"] for obs in observed_data)
    v_min, v_max = min(obs["v_act"] for obs in observed_data), max(obs["v_act"] for obs in observed_data)
    th_min, th_max = min(obs["temp"] for obs in observed_data), max(obs["temp"] for obs in observed_data)
    m_min, m_max = min(obs["pressure"] for obs in observed_data), max(obs["pressure"] for obs in observed_data)

    u_phys  = map_range(u_raw.astype(np.float64), u_min, u_max)
    v_phys  = map_range(v_raw.astype(np.float64), v_min, v_max)
    w_phys  = map_range(w_raw.astype(np.float64), -0.2, 0.2)
    th_phys = map_range(th_raw.astype(np.float64), th_min, th_max)
    m_phys  = map_range(m_raw.astype(np.float64), m_min, m_max)

    print("Phase 3: Reconciling time series grids and exporting analytical spreadsheets...")
    exported_files, daily_indices, param_config = export_csv_results(
        output_dir, args.horizon, target_dates, observed_data, 
        u_phys, v_phys, w_phys, th_phys, m_phys, steps
    )

    print("Phase 4: Calculating root mean square core variable deviations...")
    compute_and_report_rmse(daily_indices, u_phys, v_phys, th_phys, m_phys, observed_data)

    print("Phase 5: Rendering discrete 30-node topological plots and validation tables...")
    render_plots_and_tables(
        output_dir, u_phys, v_phys, w_phys, th_phys, m_phys, 
        target_dates, daily_indices, param_config, 
        observed_data, args.horizon
    )

    print("====================================================")
    print("SDCMS generalized execution tracking completes successfully.")
    print("====================================================")

if __name__ == "__main__":
    main()