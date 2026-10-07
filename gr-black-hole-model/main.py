import numpy as np
import csv
import config
from sdc_solver import run_solver
from visualizer import render_plots

def main():
    print("====================================================")
    print("Initializing Model #13: Spacetime Curvature Perturbations")
    print("====================================================")
    
    params = config.load_system_data()
    initial_state = [params["psi_init"], params["p_init"]]
    
    print(f"Initial Amplitude : {params['psi_init']}")
    print(f"Initial Momentum  : {params['p_init']}")
    print(f"Radial Distance   : {params['r_radius']} m")
    print(f"Black Hole Mass   : {config.BH_MASS} kg")
    print("====================================================")
    
    trajectory = run_solver(
        initial_state=initial_state,
        steps=config.TOTAL_STEPS,
        dt=config.DT,
        mass=config.BH_MASS,
        l_mode=config.MULTIPOLE_L,
        c=config.C_LIGHT,
        g=config.G_CONST,
        r_radius=params["r_radius"]
    )
    
    # Export CSV data
    with open(config.OUTPUT_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["step", "psi", "p_psi"])
        for idx, row in enumerate(trajectory):
            writer.writerow([idx, row[0], row[1]])
            
    render_plots(trajectory, config.DT)
    print("Model #13 execution completed successfully!")

if __name__ == "__main__":
    main()