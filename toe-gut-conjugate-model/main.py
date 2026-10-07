import numpy as np
import csv
import config
from sdc_solver import run_solver
from visualizer import render_plots

def main():
    print("====================================================")
    print("Initializing TOE / GUT Conjugate Synthesis Model")
    print("====================================================")
    
    params = config.load_system_data()
    initial_state = [
        params["psi_gr_init"], 
        params["p_gr_init"], 
        params["psi_qm_real_init"], 
        params["psi_qm_imag_init"]
    ]
    
    print(f"GR Initial Amplitude : {params['psi_gr_init']}")
    print(f"GR Initial Momentum  : {params['p_gr_init']}")
    print(f"QM Initial Real      : {params['psi_qm_real_init']}")
    print(f"QM Initial Imag      : {params['psi_qm_imag_init']}")
    print(f"Coupling Lambda      : {config.COUPLING_LAMBDA}")
    print("====================================================")
    
    trajectory = run_solver(
        initial_state=initial_state,
        steps=config.TOTAL_STEPS,
        dt=config.DT,
        lam=config.COUPLING_LAMBDA
    )
    
    # Export CSV data
    with open(config.OUTPUT_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["step", "psi_gr", "p_gr", "psi_qm_real", "psi_qm_imag"])
        for idx, row in enumerate(trajectory):
            writer.writerow([idx, row[0], row[1], row[2], row[3]])
            
    render_plots(trajectory, config.DT)
    print("TOE / GUT Conjugate Model execution completed successfully!")

if __name__ == "__main__":
    main()