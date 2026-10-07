# visualizer.py
import matplotlib.pyplot as plt
import numpy as np

def render_plots(trajectory, dt, total_days, output_dir="."):
    """
    Renders 3D Phase-Space Trajectory and 2D System Evolution plots as 
    perfect equal-sized squares fitting the portrait A4 layout.
    """
    steps = len(trajectory)
    time_days = np.arange(steps) * dt / 86400.0
    
    var1 = trajectory[:, 0]
    var2 = trajectory[:, 1]
    var3 = trajectory[:, 2]
    
    # Extract Discrete Daily Checkpoints
    daily_indices = [0]
    for d in range(1, int(np.round(total_days)) + 1):
        idx = (np.abs(time_days - d)).argmin()
        daily_indices.append(idx)

    # Perfect Square Dimensions: Equal width and height
    square_size = (11.6929 * 0.5) * 0.9

    # 1. 3D Phase-Space Trajectory Rendering (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111, projection='3d')
    
    ax_ps.plot(var1, var2, var3, color='#e74c3c', linewidth=1.0, label='Phase Trajectory')
    
    v1_daily = var1[daily_indices]
    v2_daily = var2[daily_indices]
    v3_daily = var3[daily_indices]
    
    ax_ps.scatter(v1_daily, v2_daily, v3_daily, color='#c0392b', s=15, label='Daily Checkpoints', zorder=4)
    ax_ps.scatter([var1[0]], [var2[0]], [var3[0]], color='blue', s=40, label='Initial (Day 0)', zorder=5)
    ax_ps.scatter([var1[-1]], [var2[-1]], [var3[-1]], color='black', s=40, label=f'Final (Day {int(total_days)})', zorder=5)
    
    ax_ps.set_title(f"3D Phase-Space Trajectory ({int(total_days)}-Day)", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel("State $x_1$", fontsize=8, labelpad=5)
    ax_ps.set_ylabel("State $x_2$", fontsize=8, labelpad=5)
    ax_ps.set_zlabel("State $x_3$", fontsize=8, labelpad=5)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper left', fontsize=7)
    
    ps_file = f"{output_dir}/phase_space_trajectory.png"
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. 2D System Evolution Subplots (Square)
    fig_2d, (ax1, ax2) = plt.subplots(2, 1, figsize=(square_size, square_size), sharex=True)
    
    ax1.plot(time_days, var1 / 1e9, color='#2980b9', linewidth=1.2, label='Primary State Variable ($x_1$)')
    ax1.scatter(time_days[daily_indices], var1[daily_indices] / 1e9, color='#16a085', s=15, zorder=4)
    ax1.set_ylabel("Metric ($10^9$ m)", fontsize=8, fontweight='bold')
    ax1.set_title("System Evolution Dynamics ($x_1$)", fontsize=9, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.tick_params(axis='both', labelsize=7)
    ax1.legend(loc='upper left', fontsize=7)

    ax2.plot(time_days, var2 / 1e6, color='#8e44ad', linewidth=1.2, label='Secondary State Variable ($x_2$)')
    ax2.scatter(time_days[daily_indices], var2[daily_indices] / 1e6, color='#d35400', s=15, zorder=4)
    ax2.set_xlabel("Time (Days)", fontsize=8, fontweight='bold')
    ax2.set_ylabel("Metric ($10^6$ m)", fontsize=8, fontweight='bold')
    ax2.set_title("System Evolution Dynamics ($x_2$)", fontsize=9, fontweight='bold')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.tick_params(axis='both', labelsize=7)
    ax2.legend(loc='upper left', fontsize=7)

    ts_file = f"{output_dir}/system_evolution.png"
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    print(f"Exported standardized square plots: {ps_file}, {ts_file}")