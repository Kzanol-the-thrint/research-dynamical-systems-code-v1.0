import os
import csv
import numpy as np

def export_csv_results(output_dir, steps, trajectory):
    """
    Exports Schwarzschild orbital trajectory simulation results to CSV.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "output_schwarzschild_data.csv")

    with open(output_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["step", "r_position_m", "phi_angle_rad", "r_velocity_ms", "phi_velocity_rads", "cartesian_x_m", "cartesian_y_m"])
        
        for i in range(steps):
            r, phi, rd, phd = trajectory[i]
            x = r * np.cos(phi)
            y = r * np.sin(phi)
            writer.writerow([i, f"{r:.6e}", f"{phi:.6e}", f"{rd:.6e}", f"{phd:.6e}", f"{x:.6e}", f"{y:.6e}"])

    return output_path