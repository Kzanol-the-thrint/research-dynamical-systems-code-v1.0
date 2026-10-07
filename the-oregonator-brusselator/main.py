import csv
import config
from matrix import create_sdc_matrix
from sdc_solver import run_sdc_solver
from visualizer import render_plots

def save_trajectory_to_csv(trajectory, dt, output_csv):
    """Writes computed state trajectories from memory to universal CSV format."""
    steps = len(trajectory)
    dim = trajectory.shape[1]
    
    with open(output_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        headers = ["step", "time"] + [f"state_{i}" for i in range(dim)]
        writer.writerow(headers)
        
        for i in range(steps):
            t_val = i * dt
            writer.writerow([i, t_val] + trajectory[i].tolist())
            
    print(f"Full trajectory written to '{output_csv}'.")

def main():
    params = config.load_system_data()

    x0 = params.get("x0", 0.0)
    x1 = params.get("x1", 0.0)
    x2 = params.get("x2", 0.0)
    
    print("====================================================")
    print("Initializing Universal SDCM Engine...")
    print(f"Forecast Horizon : {config.HORIZON}")
    print(f"Time Step (dt)   : {config.DT}")
    print(f"Initial Vector   : [{x0}, {x1}, {x2}]")
    print("====================================================")

    # Build universal matrix operator map
    matrix_map = create_sdc_matrix(params)

    # Initial State Vector Dynamic Allocation
    initial_state = [x0, x1, x2]

    # 1. Run numerical solver core
    trajectory, steps = run_sdc_solver(
        matrix_map, 
        initial_state, 
        total_steps=config.HORIZON, 
        dt=config.DT
    )

    # 2. Render plots universally
    render_plots(trajectory, config.DT, config.HORIZON, initial_state)

    # 3. Export data log to CSV
    save_trajectory_to_csv(trajectory, config.DT, config.OUTPUT_FILE)

    # Terminal summary output
    final_state = trajectory[-1]
    print("\nSimulation execution complete over", steps, "steps.")
    print("----------------------------------------------------")
    for idx, val in enumerate(final_state):
        print(f"State Variable [{idx}] : Initial = {initial_state[idx]:,.2f} | Final = {val:,.2f}")
    print("----------------------------------------------------")

if __name__ == "__main__":
    main()