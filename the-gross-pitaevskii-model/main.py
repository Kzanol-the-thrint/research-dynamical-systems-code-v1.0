import os
from config import DT, TOTAL_STEPS, POTENTIAL_V0, NONLINEAR_G, load_system_data
from sdc_solver import run_solver
from visualizer import render_plots

def main():
    print("Initializing Gross-Pitaevskii Nonlinear Quantum Simulation...")
    
    # Load parameters and initial state
    data = load_system_data()
    initial_state = [data["psi_real_init"], data["psi_imag_init"]]
    
    # Run the SDC matrix differential equation solver
    print(f"Running simulation for {TOTAL_STEPS} steps with dt={DT}...")
    trajectory = run_solver(initial_state, TOTAL_STEPS, DT, POTENTIAL_V0, NONLINEAR_G)
    
    print(f"Simulation complete. Final State Vector: {trajectory[-1]}")
    
    # Render and export visualization plots
    output_dir = "."
    render_plots(trajectory, DT, output_dir=output_dir)

if __name__ == "__main__":
    main()