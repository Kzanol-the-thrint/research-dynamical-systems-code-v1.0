# visualizer.py
import os
import matplotlib.pyplot as plt
import numpy as np

def render_plots(trajectory, dt, total_days, output_dir="."):
    """
    Renders 3D Phase-Space Lorenz Attractor and 2D System Evolution plots as 
    perfect equal-sized squares fitting the portrait A4 layout with robust path handling.
    """
    steps = len(trajectory)
    time_units = np.arange(steps) * dt
    
    x = trajectory[:, 0]
    y = trajectory[:, 1]
    z = trajectory[:, 2]

    # Perfect Square Dimensions: Equal width and height (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # Ensure output directory exists securely
    os.makedirs(output_dir, exist_ok=True)

    # 1. 3D Lorenz Strange Attractor Rendering (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111, projection='3d')
    
    ax_ps.plot(x, y, z, color='#8e44ad', linewidth=0.8, label='Lorenz Trajectory')
    ax_ps.scatter([x[0]], [y[0]], [z[0]], color='blue', s=40, label='Initial State', zorder=5)
    ax_ps.scatter([x[-1]], [y[-1]], [z[-1]], color='red', s=40, label='Final State', zorder=5)
    
    ax_ps.set_title("3D Lorenz Strange Attractor Phase-Space", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel("x (Convection)", fontsize=8, labelpad=5)
    ax_ps.set_ylabel("y (Temperature)", fontsize=8, labelpad=5)
    ax_ps.set_zlabel("z (Distortion)", fontsize=8, labelpad=5)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper left', fontsize=7)
    
    ps_file = os.path.join(output_dir, "phase_space_trajectory.png")
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. 2D System Evolution Subplots (Square, 3 subplots stacked vertically)
    fig_2d, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(square_size, square_size), sharex=True)
    
    ax1.plot(time_units, x, color='#e74c3c', linewidth=1.0, label='x (Convection)')
    ax1.set_ylabel("x", fontsize=8, fontweight='bold')
    ax1.set_title("Lorenz System Evolution Dynamics", fontsize=9, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.tick_params(axis='both', labelsize=7)
    ax1.legend(loc='upper left', fontsize=7)

    ax2.plot(time_units, y, color='#2980b9', linewidth=1.0, label='y (Temperature)')
    ax2.set_ylabel("y", fontsize=8, fontweight='bold')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.tick_params(axis='both', labelsize=7)
    ax2.legend(loc='upper left', fontsize=7)

    ax3.plot(time_units, z, color='#27ae60', linewidth=1.0, label='z (Distortion)')
    ax3.set_xlabel("Time Units ($t$)", fontsize=8, fontweight='bold')
    ax3.set_ylabel("z", fontsize=8, fontweight='bold')
    ax3.grid(True, linestyle='--', alpha=0.6)
    ax3.tick_params(axis='both', labelsize=7)
    ax3.legend(loc='upper left', fontsize=7)

    ts_file = os.path.join(output_dir, "system_evolution.png")
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    print(f"Exported standardized Lorenz square plots: {ps_file}, {ts_file}")