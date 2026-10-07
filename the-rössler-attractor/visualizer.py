import matplotlib.pyplot as plt
import numpy as np

def render_plots(trajectory, time_steps, output_dir="."):
    """
    Renders 3D Rössler Attractor Phase-Space and 2D System Evolution time-series plots 
    as perfect equal-sized squares fitting the portrait A4 layout.
    """
    x = trajectory[:, 0]
    y = trajectory[:, 1]
    z = trajectory[:, 2]
    
    # Perfect Square Dimensions: Equal width and height (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. 3D Phase Space Attractor (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111, projection='3d')
    
    ax_ps.plot(x, y, z, color='teal', lw=0.8, label="SDC Rössler Attractor")
    ax_ps.scatter([x[0]], [y[0]], [z[0]], color='blue', s=30, label="Initial State", zorder=5)
    ax_ps.scatter([x[-1]], [y[-1]], [z[-1]], color='black', s=30, label="Final State", zorder=5)
    
    ax_ps.set_title("Rössler Attractor 3D Phase Space", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel("X Axis", fontsize=8, labelpad=5)
    ax_ps.set_ylabel("Y Axis", fontsize=8, labelpad=5)
    ax_ps.set_zlabel("Z Axis", fontsize=8, labelpad=5)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper left', fontsize=7)
    
    ps_file = f"{output_dir}/phase_space_trajectory.png"
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. Time-Series Dynamics (Square)
    fig_2d, ax_ts = plt.subplots(figsize=(square_size, square_size))
    
    ax_ts.plot(time_steps, x, color='tab:blue', lw=1.2, label="X Variable")
    ax_ts.plot(time_steps, y, color='tab:orange', lw=1.2, label="Y Variable")
    ax_ts.plot(time_steps, z, color='tab:green', lw=1.2, label="Z Variable")
    
    ax_ts.set_title("Rössler Variables Over Time", fontsize=9, fontweight='bold')
    ax_ts.set_xlabel("Time Units ($t$)", fontsize=8, labelpad=5)
    ax_ts.set_ylabel("Amplitude", fontsize=8, labelpad=5)
    ax_ts.grid(True, linestyle='--', alpha=0.6)
    ax_ts.tick_params(axis='both', labelsize=7)
    ax_ts.legend(loc='upper right', fontsize=7)

    ts_file = f"{output_dir}/system_evolution.png"
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    print(f"Exported standardized Rössler square plots: {ps_file}, {ts_file}")