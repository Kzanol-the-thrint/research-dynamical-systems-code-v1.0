import matplotlib.pyplot as plt
import numpy as np

def render_plots(trajectory, dt, horizon, initial_state, output_dir="."):
    """
    Renders universal 3D Phase-Space Trajectory and 2D System Evolution plots, 
    along with a formatted text summary image, as perfect equal-sized squares 
    fitting the portrait A4 layout.
    """
    steps = len(trajectory)
    time_steps = np.arange(steps) * dt
    
    dim = trajectory.shape[1]
    v0 = trajectory[:, 0]
    v1 = trajectory[:, 1]
    v2 = trajectory[:, 2] if dim > 2 else np.zeros_like(v0)
    
    # Perfect Square Dimensions: Equal width and height (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. 3D Phase-Space Attractor Portrait (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111, projection='3d')
    
    ax_ps.plot(v0, v1, v2, color='#e74c3c', linewidth=1.2, label='State Trajectory')
    ax_ps.scatter([v0[0]], [v1[0]], [v2[0]], color='blue', s=40, label=r'Initial State ($\Phi_0$)', zorder=5)
    ax_ps.scatter([v0[-1]], [v1[-1]], [v2[-1]], color='black', s=40, label=r'Final State ($\Phi_f$)', zorder=5)
    
    ax_ps.set_title("3D Phase-Space Attractor Portrait", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel("State Variable 0", fontsize=8, labelpad=5)
    ax_ps.set_ylabel("State Variable 1", fontsize=8, labelpad=5)
    ax_ps.set_zlabel("State Variable 2", fontsize=8, labelpad=5)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper left', fontsize=7)
    
    ps_file = f"{output_dir}/phase_space_trajectory.png"
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. 2D Multi-Variable Curves Over Time (Square)
    fig_2d, ax = plt.subplots(figsize=(square_size, square_size))
    
    ax.plot(time_steps, v0, color='#2980b9', linewidth=1.4, label='State [0]')
    ax.plot(time_steps, v1, color='#e74c3c', linewidth=1.4, label='State [1]')
    if dim > 2:
        ax.plot(time_steps, v2, color='#27ae60', linewidth=1.4, label='State [2]')
    
    ax.set_xlabel("Time Steps", fontsize=8, fontweight='bold')
    ax.set_ylabel("Magnitude", fontsize=8, fontweight='bold')
    ax.set_title("Universal System Dynamics Over Time", fontsize=9, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.tick_params(axis='both', labelsize=7)
    ax.legend(loc='upper right', fontsize=7)

    ts_file = f"{output_dir}/system_evolution.png"
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    print(f"Exported standardized Oregonator-Brusselator square plots: {ps_file}, {ts_file}")

    # 3. Formatted Text Summary Image Output
    final_state = trajectory[-1]
    summary_lines = [
        "====================================================",
        "Initializing Universal SDCM Engine...",
        f"Forecast Horizon : {horizon}",
        f"Time Step (dt)   : {dt}",
        f"Initial Vector   : [{initial_state[0]:,.1f}, {initial_state[1]:,.1f}, {initial_state[2]:,.1f}]",
        "====================================================",
        f"Simulation execution complete over {steps} steps.",
        "----------------------------------------------------"
    ]
    for idx, val in enumerate(final_state):
        summary_lines.append(f"State Variable [{idx}] : Initial = {initial_state[idx]:,.2f} | Final = {val:,.2f}")
    summary_lines.append("----------------------------------------------------")
    
    summary_text = "\n".join(summary_lines)

    fig_txt, ax_txt = plt.subplots(figsize=(8, 4.5))
    ax_txt.axis('off')
    ax_txt.text(0.05, 0.95, summary_text, transform=ax_txt.transAxes,
                fontsize=10, family='monospace', verticalalignment='top',
                bbox=dict(boxstyle='round,pad=0.8', facecolor='#f8f9fa', edgecolor='#ced4da'))
    
    sum_file = f"{output_dir}/system_summary_table.png"
    plt.tight_layout()
    plt.savefig(sum_file, dpi=300)
    plt.close(fig_txt)
    print(f"Exported Text Summary PNG: {sum_file}")