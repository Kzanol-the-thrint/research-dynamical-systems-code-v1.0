import numpy as np
import csv
from config import load_system_data, OUTPUT_FILE, DT, HORIZON
from sdc_solver import SDCSolver
from visualizer import render_plots

def main():
    print("==================================================")
    print("Initializing Universal SDC Engine: Rössler Attractor...")
    print(f"Forecast Horizon : {HORIZON}")
    print(f"Time Step (dt)   : {DT}")
    
    params = load_system_data()
    params["dt"] = DT
    params["horizon"] = HORIZON
    
    initial_vector = [params.get("x0", 0.1), params.get("x1", 0.0), params.get("x2", 0.0), params.get("x3", 1.0)]
    print(f"Initial Vector   : {initial_vector}")
    print("==================================================")
    
    solver = SDCSolver(params)
    trajectory = solver.run_simulation()
    steps_count = len(trajectory)
    
    time_steps = np.linspace(0, HORIZON, steps_count)
    
    with open(OUTPUT_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Step", "Time", "X", "Y", "Z", "Anchor"])
        for idx, (t, state) in enumerate(zip(time_steps, trajectory)):
            writer.writerow([idx, f"{t:.4f}", f"{state[0]:.6f}", f"{state[1]:.6f}", f"{state[2]:.6f}", f"{state[3]:.6f}"])
            
    render_plots(trajectory, time_steps)
    
    print(f"Simulation execution complete over {steps_count} steps.")
    print("--------------------------------------------------")
    print(f"X Variable         : Initial = {initial_vector[0]:.2f} | Final = {trajectory[-1, 0]:.2f}")
    print(f"Y Variable         : Initial = {initial_vector[1]:.2f} | Final = {trajectory[-1, 1]:.2f}")
    print(f"Z Variable         : Initial = {initial_vector[2]:.2f} | Final = {trajectory[-1, 2]:.2f}")
    print(f"Full trajectory exported to '{OUTPUT_FILE}'.")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()