import csv
import config
from matrix import create_sdc_matrix, create_sdc_matrix
from sdc_solver import run_sdc_solver
from visualizer import render_plots

def save_trajectory_to_csv(trajectory, dt, output_csv):
    """Writes computed 1PN relativistic trajectory data from memory to CSV."""
    steps = len(trajectory)
    
    with open(output_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["step", "time_sec", "r12", "r23", "r31", "p12", "p23", "p31"])
        
        for i in range(steps):
            time_sec = i * dt
            writer.writerow([i, time_sec] + trajectory[i].tolist())
            
    print(f"Full 1PN trajectory written to '{output_csv}'.")

def main():
    # Load physical metrics from input_data.csv
    phys_data = config.load_system_data()

    m1 = phys_data["m1"]
    m2 = phys_data["m2"]
    m3 = phys_data["m3"]

    print("====================================================")
    print("Initializing Post-Newtonian (1PN) Celestial SDC Engine...")
    print(f"Forecast Horizon : {config.DAYS} Days")
    print(f"Time Step (dt)   : {config.DT} Seconds")
    print(f"Speed of Light   : {config.C_LIGHT:.3e} m/s")
    print(f"System Masses    : m1={m1:.3e}, m2={m2:.3e}, m3={m3:.3e}")
    print("====================================================")

    # Build 1PN matrix operator
    matrix_map = create_sdc_matrix(m1, m2, m3, config.DT)

    # Convert initial velocities into canonical momenta (p = m * v)
    initial_p12 = m2 * phys_data["v12"]
    initial_p23 = m3 * phys_data["v23"]
    initial_p31 = m3 * phys_data["v31"]

    # Initial Conjugate State Vector: [r12, r23, r31, p12, p23, p31]
    initial_state = [
        phys_data["r12"], 
        phys_data["r23"], 
        phys_data["r31"], 
        initial_p12, 
        initial_p23, 
        initial_p31
    ]

    # 1. Run 1PN numerical solver in RAM
    trajectory, steps = run_sdc_solver(
        matrix_map, 
        initial_state, 
        total_days=config.DAYS, 
        dt=config.DT
    )

    # 2. Render 1PN plots directly from memory
    render_plots(trajectory, config.DT, config.DAYS)

    # 3. Export full 1PN trajectory to CSV
    save_trajectory_to_csv(trajectory, config.DT, config.OUTPUT_FILE)

    # 4. Compute absolute and signed deltas
    r12_init, r12_final = trajectory[0, 0], trajectory[-1, 0]
    r23_init, r23_final = trajectory[0, 1], trajectory[-1, 1]
    r31_init, r31_final = trajectory[0, 2], trajectory[-1, 2]

    # Terminal summary output
    print("\n1PN Simulation complete over", steps, "discrete steps.")
    print("----------------------------------------------------")
    print(f"1PN Earth-Sun (r12) : Initial = {r12_init:,.2f} m | Final = {r12_final:,.2f} m | Delta = {r12_final - r12_init:+,.2f} m | Abs Delta = {abs(r12_final - r12_init):,.2f} m")
    print(f"1PN Earth-Moon(r23) : Initial = {r23_init:,.2f} m | Final = {r23_final:,.2f} m | Delta = {r23_final - r23_init:+,.2f} m | Abs Delta = {abs(r23_final - r23_init):,.2f} m")
    print(f"1PN Sun-Moon  (r31) : Initial = {r31_init:,.2f} m | Final = {r31_final:,.2f} m | Delta = {r31_final - r31_init:+,.2f} m | Abs Delta = {abs(r31_final - r31_init):,.2f} m")
    print("----------------------------------------------------")

if __name__ == "__main__":
    main()