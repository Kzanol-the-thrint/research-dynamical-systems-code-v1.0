# main.py
import os
import csv
import config
from matrix import create_sdc_matrix
from sdc_solver import run_sdc_solver
from visualizer import render_plots

def save_trajectory_to_csv(trajectory, dt, output_csv):
    """Writes computed Lorenz trajectory data from memory to CSV securely."""
    steps = len(trajectory)
    os.makedirs(os.path.dirname(os.path.abspath(output_csv)), exist_ok=True)
    
    with open(output_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["step", "time", "x", "y", "z"])
        
        for i in range(steps):
            t = i * dt
            writer.writerow([i, t] + trajectory[i].tolist())
            
    print(f"Full trajectory written to '{output_csv}'.")

def main():
    # Load parameters from configuration/CSV
    data = config.load_system_data()

    sigma = data.get("sigma", 10.0)
    rho = data.get("rho", 28.0)
    beta = data.get("beta", 8/3)
    
    x0 = data.get("x", 1.0)
    y0 = data.get("y", 1.0)
    z0 = data.get("z", 1.0)

    print("====================================================")
    print("Initializing Autonomous Lorenz SDC Matrix Engine...")
    print(f"Forecast Horizon : {config.DAYS} Time Units")
    print(f"Time Step (dt)   : {config.DT}")
    print(f"Parameters       : sigma={sigma}, rho={rho}, beta={beta:.4f}")
    print("====================================================")

    # Build time-folded matrix operator map
    matrix_map = create_sdc_matrix(sigma, rho, beta, config.DT)

    # Initial State Vector: [x, y, z]
    initial_state = [x0, y0, z0]

    # 1. Run SDC solver in RAM
    trajectory, steps = run_sdc_solver(
        matrix_map, 
        initial_state, 
        total_days=config.DAYS, 
        dt=config.DT
    )

    # 2. Render standardized plots directly from memory
    render_plots(trajectory, config.DT, config.DAYS, output_dir=".")

    # 3. Export full trajectory to CSV
    save_trajectory_to_csv(trajectory, config.DT, config.OUTPUT_FILE)

    # Terminal summary output
    print("\nSimulation complete over", steps, "discrete steps.")
    print("----------------------------------------------------")
    print(f"Final State -> x: {trajectory[-1, 0]:.4f} | y: {trajectory[-1, 1]:.4f} | z: {trajectory[-1, 2]:.4f}")
    print("----------------------------------------------------")

if __name__ == "__main__":
    main()