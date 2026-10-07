import numpy as np
import config
from matrix import create_sdc_matrix
from sdc_solver import run_sdc_solver
from visualizer import render_plots

def main():
    # 1. Load configuration and initial parameters
    params = config.load_system_data()
    
    horizon = params.get("horizon", 50.0)
    dt = params.get("dt", 0.05)
    
    initial_state = [
        params.get("x0", 0.1),
        params.get("x1", 0.0),
        params.get("x2", 0.0)
    ]
    
    print("====================================================")
    print("Initializing Universal SDCM Engine...")
    print(f"Forecast Horizon : {horizon}")
    print(f"Time Step (dt)   : {dt}")
    print(f"Initial Vector   : {initial_state}")
    print("====================================================")

    # 2. Construct State-Dependent Coefficient Matrix Operator Map
    matrix_map = create_sdc_matrix(params)
    
    # 3. Execute SDC Solver Integration Loop
    trajectory, total_steps = run_sdc_solver(matrix_map, initial_state, horizon, dt)
    print(f"Simulation execution complete over {total_steps} steps.")

    # 4. Export trajectories to CSV output
    output_rows = []
    for step_idx, state in enumerate(trajectory):
        output_rows.append([step_idx * dt] + list(state))
        
    import csv
    with open(config.OUTPUT_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["time", "x0", "x1", "x2"])
        writer.writerows(output_rows)
    print(f"Exported trajectory data to {config.OUTPUT_FILE}")

    # 5. Render plots universally (passing initial_state explicitly)
    render_plots(trajectory, dt, horizon, initial_state)

if __name__ == "__main__":
    main()