import matplotlib.pyplot as plt
import numpy as np

def render_plots(trajectory, dt, output_dir="."):
    """
    Renders 3D Phase-Space Trajectory and 2D System Evolution plots for the Black Hole model as 
    perfect equal-sized squares fitting the portrait A4 layout.
    """
    steps = len(trajectory)
    time_steps = np.arange(steps) * dt
    
    psi_vals = trajectory[:, 0]
    p_vals = trajectory[:, 1]
    
    checkpoint_count = min(20, steps)
    checkpoint_indices = np.linspace(0, steps - 1, checkpoint_count, dtype=int)

    # Perfect Square Dimensions: Equal width and height (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. 3D Phase-Space Manifold (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111, projection='3d')
    
    ax_ps.plot(psi_vals, p_vals, time_steps, color='#8e44ad', linewidth=1.2, label='Curvature Trajectory')
    ax_ps.scatter(psi_vals[checkpoint_indices], p_vals[checkpoint_indices], time_steps[checkpoint_indices], 
                  color='#6c3483', s=20, label='Checkpoints', zorder=4)
    ax_ps.scatter([psi_vals[0]], [p_vals[0]], [time_steps[0]], color='blue', s=40, label='Initial State', zorder=5)
    ax_ps.scatter([psi_vals[-1]], [p_vals[-1]], [time_steps[-1]], color='black', s=40, label='Final State', zorder=5)
    
    ax_ps.set_title("3D Black Hole Curvature Phase-Space Manifold", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel("Amplitude $\psi(t)$", fontsize=8, labelpad=5)
    ax_ps.set_ylabel("Momentum $p_\psi(t)$", fontsize=8, labelpad=5)
    ax_ps.set_zlabel("Time Steps", fontsize=8, labelpad=5)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper left', fontsize=7)
    
    ps_file = f"{output_dir}/phase_space_trajectory.png"
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. 2D System Evolution Subplots (Square)
    fig_2d, (ax1, ax2) = plt.subplots(2, 1, figsize=(square_size, square_size), sharex=True)
    
    ax1.plot(time_steps, psi_vals, color='#2980b9', linewidth=1.4, label='Perturbation Amplitude $\psi(t)$')
    ax1.set_ylabel("Amplitude ($\psi$)", fontsize=8, fontweight='bold')
    ax1.set_title("Black Hole Curvature Perturbation Dynamics", fontsize=9, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.tick_params(axis='both', labelsize=7)
    ax1.legend(loc='upper left', fontsize=7)

    ax2.plot(time_steps, p_vals, color='#c0392b', linewidth=1.4, label=r'Conjugate Momentum $p_\psi(t)$')
    ax2.set_xlabel("Normalized Time", fontsize=8, fontweight='bold')
    ax2.set_ylabel(r"Momentum ($p_\psi$)", fontsize=8, fontweight='bold')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.tick_params(axis='both', labelsize=7)
    ax2.legend(loc='upper left', fontsize=7)

    ts_file = f"{output_dir}/system_evolution.png"
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    print(f"Exported standardized Black Hole square plots: {ps_file}, {ts_file}")