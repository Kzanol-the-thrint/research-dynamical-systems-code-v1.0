import os
import shutil
import numpy as np
from config import load_system_data, M_CENTRAL, G_CONST, C_LIGHT, HORIZON_STEPS, DT
from matrix import create_sdc_matrix
from sdc_solver import run_schwarzschild_solver
from exporter import export_csv_results
from visualizer import render_orbital_plots

def main():
    output_dir = "data/output_schwarzschild"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    print("Phase 1: Loading initial orbital conditions and parameters...")
    system_data = load_system_data()
    initial_state = [
        system_data["r_init"],
        system_data["phi_init"],
        system_data["r_dot_init"],
        system_data["phi_dot_init"]
    ]

    print("Phase 2: Constructing Schwarzschild State-Dependent Coefficient (SDC) Matrix...")
    matrix_map = create_sdc_matrix(M_CENTRAL, G_CONST, C_LIGHT)

    print("Phase 3: Executing relativistic orbital integration steps...")
    trajectory, steps = run_schwarzschild_solver(
        matrix_map, initial_state, steps=HORIZON_STEPS, dt=DT
    )

    print("Phase 4: Exporting trajectory results to CSV...")
    exported_csv = export_csv_results(output_dir, steps, trajectory)
    print(f"Data successfully exported to {exported_csv}")

    print("Phase 5: Rendering 2D orbital trajectories and system evolution plots...")
    render_orbital_plots(output_dir, trajectory, steps)

    print("====================================================")
    print("Schwarzschild SDC Engine execution completed successfully.")
    print("====================================================")

if __name__ == "__main__":
    main()