# main.py
import csv
import config
from matrix import create_sdc_matrix
from sdc_solver import run_sdc_solver
from visualizer import render_plots, render_terminal_screenshot

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

    params = {
        "alpha": data.get("alpha", 1.0),
        "beta": data.get("beta", 0.1),
        "delta": data.get("delta", 0.075),
        "gamma": data.get("gamma", 1.5)
    }
    
    initials = {
        "x0": data.get("x0", 10.0),
        "y0": data.get("y0", 5.0)
    }

    print("====================================================")
    print("Initializing Lotka-Volterra SDC Engine...")
    print(f"Forecast Horizon : {config.TIME_HORIZON} Units")
    print(f"Time Step (dt)   : {config.DT}")
    print(f"Parameters       : alpha={params['alpha']}, beta={params['beta']}, delta={params['delta']}, gamma={params['gamma']}")
    print(f"Initial States   : Prey(X)={initials['x0']}, Predator(Y)={initials['y0']}")
    print("====================================================")

    # Build matrix operator
    matrix_map = create_sdc_matrix(params['alpha'], params['beta'], params['delta'], params['gamma'], config.DT)
    initial_state = [initials['x0'], initials['y0']]

    # 1. Run numerical solver in RAM
    trajectory, steps = run_sdc_solver(
        matrix_map, 
        initial_state, 
        total_time=config.TIME_HORIZON, 
        dt=config.DT
    )

    # 2. Render phase-space and time-series plots
    render_plots(trajectory, config.DT, config.TIME_HORIZON)

    # 3. Export full trajectory to CSV
    save_trajectory_to_csv(trajectory, config.DT, config.OUTPUT_FILE)

    # State values
    x_init, x_final = trajectory[0, 0], trajectory[-1, 0]
    y_init, y_final = trajectory[0, 1], trajectory[-1, 1]

    # Terminal summary CLI output
    print("\nSimulation complete over", steps, "discrete steps.")
    print("----------------------------------------------------")
    print(f"Prey (X)      : Initial = {x_init:.3f} | Final = {x_final:.3f}")
    print(f"Predator (Y)  : Initial = {y_init:.3f} | Final = {y_final:.3f}")
    print("----------------------------------------------------")

    # 4. Export terminal output screenshot PNG
    render_terminal_screenshot(
        params_dict=params,
        initial_dict=initials,
        steps=steps,
        x_init=x_init,
        x_final=x_final,
        y_init=y_init,
        y_final=y_final
    )

if __name__ == "__main__":
    main()