import numpy as np
import csv
import config
from sdc_solver import run_solver
from visualizer import render_plots

def main():
    print("====================================================")
    print("Initializing Model #14: Nonlinear Quantum Mechanics")
    print("====================================================")
    
    params = config.load_system_data()
    initial_state = [params["psi_real_init"], params["psi_imag_init"]]
    
    print(f"Initial Re(psi)   : {params['psi_real_init']}")
    print(f"Initial Im(psi)   : {params['psi_imag_init']}")
    print(f"Potential V0      : {config.POTENTIAL_V0}")
    print(f"Interaction g     : {config.NONLINEAR_G}")
    print("====================================================")
    
    trajectory = run_solver(
        initial_state=initial_state,
        steps=config.TOTAL_STEPS,
        dt=config.DT,
        v0=config.POTENTIAL_V0,
        g=config.NONLINEAR_G
    )
    
    # Export CSV data
    with open(config.OUTPUT_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["step", "psi_real", "psi_imag"])
        for idx, row in enumerate(trajectory):
            writer.writerow([idx, row[0], row[1]])
            
    render_plots(trajectory, config.DT)
    print("Model #14 execution completed successfully!")

if __name__ == "__main__":
    main()