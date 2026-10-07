import numpy as np
import csv
from config import load_system_data, OUTPUT_FILE, DT, HORIZON
from sdc_solver import SDCSolver
from visualizer import render_plots

def main():
    print("==================================================")
    print("Initializing Universal SDC Engine: FitzHugh-Nagumo...")
    print(f"Forecast Horizon : {HORIZON}")
    print(f"Time Step (dt)   : {DT}")
    
    params = load_system_data()
    params["dt"] = DT
    params["horizon"] = HORIZON
    
    initial_vector = [params.get("x0", -1.0), params.get("x1", 1.0), params.get("x2", 1.0)]
    print(f"Initial Vector   : {initial_vector}")
    print("==================================================")
    
    solver = SDCSolver(params)
    trajectory = solver.run_simulation()
    steps_count = len(trajectory)
    
    time_steps = np.linspace(0, HORIZON, steps_count)
    
    with open(OUTPUT_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Step", "Time", "Voltage (v)", "Recovery (w)", "Anchor (x2)"])
        for idx, (t, state) in enumerate(zip(time_steps, trajectory)):
            writer.writerow([idx, f"{t:.4f}", f"{state[0]:.6f}", f"{state[1]:.6f}", f"{state[2]:.6f}"])
            
    render_plots(trajectory, time_steps)
    
    print(f"Simulation execution complete over {steps_count} steps.")
    print("--------------------------------------------------")
    print(f"Voltage (v)       : Initial = {initial_vector[0]:.2f} | Final = {trajectory[-1, 0]:.2f}")
    print(f"Recovery (w)      : Initial = {initial_vector[1]:.2f} | Final = {trajectory[-1, 1]:.2f}")
    print(f"Full trajectory exported to '{OUTPUT_FILE}'.")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()