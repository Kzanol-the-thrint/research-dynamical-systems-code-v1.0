# main.py
import csv
import config
from matrix import create_sdc_matrix
from sdc_solver import run_sdc_solver
from visualizer import render_lv_plots

def save_trajectory_to_csv(trajectory, dt, output_csv):
    """Writes computed ecological trajectory data to CSV."""
    steps = len(trajectory)
    with open(output_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["step", "time", "prey_x", "predator_y"])
        
        for i in range(steps):
            time_val = i * dt
            writer.writerow([i, time_val] + trajectory[i].tolist())
            
    print(f"Full trajectory written to '{output_csv}'.")

def main():
    # Load ecological parameters and initial populations
    data = config.load_system_data()

    alpha = data.get("alpha", 1.0)
    beta = data.get("beta", 0.1)
    delta = data.get("delta", 0.075)
    gamma = data.get("gamma", 1.5)
    
    x0 = data.get("x0", 10.0)
    y0 = data.get("y0", 5.0)

    print("====================================================")
    print("Initializing Lotka-Volterra SDC Engine...")
    print(f"Forecast Horizon : {config.TIME_HORIZON} Units")
    print(f"Time Step (dt)   : {config.DT}")
    print(f"Parameters       : alpha={alpha}, beta={beta}, delta={delta}, gamma={gamma}")
    print(f"Initial States   : Prey(X)={x0}, Predator(Y)={y0}")
    print("====================================================")

    # Build matrix operator
    matrix_map = create_sdc_matrix(alpha, beta, delta, gamma, config.DT)
    initial_state = [x0, y0]

    # 1. Run numerical solver in RAM
    trajectory, steps = run_sdc_solver(
        matrix_map, 
        initial_state, 
        total_time=config.TIME_HORIZON, 
        dt=config.DT
    )

    # 2. Render phase-space and time-series plots
    render_lv_plots(trajectory, config.DT, config.TIME_HORIZON)

    # 3. Export full trajectory to CSV
    save_trajectory_to_csv(trajectory, config.DT, config.OUTPUT_FILE)

    # Terminal summary output
    x_init, x_final = trajectory[0, 0], trajectory[-1, 0]
    y_init, y_final = trajectory[0, 1], trajectory[-1, 1]

    print("\nSimulation complete over", steps, "discrete steps.")
    print("----------------------------------------------------")
    print(f"Prey (X)      : Initial = {x_init:.3f} | Final = {x_final:.3f}")
    print(f"Predator (Y)  : Initial = {y_init:.3f} | Final = {y_final:.3f}")
    print("----------------------------------------------------")

if __name__ == "__main__":
    main()