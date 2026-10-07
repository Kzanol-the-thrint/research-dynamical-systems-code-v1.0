import matplotlib.pyplot as plt
import numpy as np

def render_plots(trajectory, dt, total_days, output_dir="."):
    """
    Renders 3D Post-Newtonian Relativistic Phase-Space Trajectory and 2D Separation Evolution plots 
    as perfect equal-sized squares fitting the portrait A4 layout.
    """
    steps = len(trajectory)
    time_days = np.arange(steps) * dt / 86400.0
    
    r12 = trajectory[:, 0]
    r23 = trajectory[:, 1]
    r31 = trajectory[:, 2]
    
    daily_indices = [0]
    for d in range(1, int(np.round(total_days)) + 1):
        idx = (np.abs(time_days - d)).argmin()
        daily_indices.append(idx)

    # Perfect Square Dimensions: Equal width and height (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. 3D Phase-Space Trajectory Rendering (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111, projection='3d')
    
    ax_ps.plot(r12, r23, r31, color='#8e44ad', linewidth=1.2, label='1PN Relativistic Trajectory')
    ax_ps.scatter(r12[daily_indices], r23[daily_indices], r31[daily_indices], color='#6c3483', s=20, label='Daily Checkpoints', zorder=4)
    ax_ps.scatter([r12[0]], [r23[0]], [r31[0]], color='blue', s=40, label='Initial State (Day 0)', zorder=5)
    ax_ps.scatter([r12[-1]], [r23[-1]], [r31[-1]], color='black', s=40, label=f'Final State (Day {int(total_days)})', zorder=5)
    
    ax_ps.set_title(f"3D Post-Newtonian Phase-Space ({int(total_days)}-Day)", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel("r12 (m)", fontsize=8, labelpad=5)
    ax_ps.set_ylabel("r23 (m)", fontsize=8, labelpad=5)
    ax_ps.set_zlabel("r31 (m)", fontsize=8, labelpad=5)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper left', fontsize=7)
    
    ps_file = f"{output_dir}/phase_space_trajectory.png"
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. 2D System Evolution Subplots (Square)
    fig_2d, (ax1, ax2) = plt.subplots(2, 1, figsize=(square_size, square_size), sharex=True)
    
    ax1.plot(time_days, r12 / 1e9, color='#e67e22', linewidth=1.4, label='1PN r12 (Earth-Sun)')
    ax1.set_ylabel("Distance ($10^9$ m)", fontsize=8, fontweight='bold')
    ax1.set_title("1PN Separation Dynamics Over Time", fontsize=9, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.tick_params(axis='both', labelsize=7)
    ax1.legend(loc='upper left', fontsize=7)

    ax2.plot(time_days, r23 / 1e6, color='#27ae60', linewidth=1.4, label='1PN r23 (Earth-Moon)')
    ax2.set_xlabel("Time (Days)", fontsize=8, fontweight='bold')
    ax2.set_ylabel("Distance ($10^6$ m)", fontsize=8, fontweight='bold')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.tick_params(axis='both', labelsize=7)
    ax2.legend(loc='upper left', fontsize=7)

    ts_file = f"{output_dir}/system_evolution.png"
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    print(f"Exported standardized Relativistic Three-Body square plots: {ps_file}, {ts_file}")