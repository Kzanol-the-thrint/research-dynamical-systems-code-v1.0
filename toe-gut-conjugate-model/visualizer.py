import matplotlib.pyplot as plt
import numpy as np

def render_plots(trajectory, dt, output_dir="."):
    """
    Renders Unified TOE/GUT 3D Phase-Space Manifold and 2D Conjugate Field Interaction plots 
    as perfect equal-sized squares fitting the portrait A4 layout.
    """
    steps = len(trajectory)
    time_steps = np.arange(steps) * dt
    
    psi_gr = trajectory[:, 0]
    p_gr = trajectory[:, 1]
    q_real = trajectory[:, 2]
    q_imag = trajectory[:, 3]
    
    checkpoint_count = min(25, steps)
    checkpoint_indices = np.linspace(0, steps - 1, checkpoint_count, dtype=int)

    # Perfect Square Dimensions: Equal width and height (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. Unified 3D Phase-Space Manifold (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111, projection='3d')
    
    ax_ps.plot(psi_gr, p_gr, time_steps, color='#8e44ad', linewidth=1.2, label='Conjugate GR Trajectory')
    ax_ps.scatter(psi_gr[checkpoint_indices], p_gr[checkpoint_indices], time_steps[checkpoint_indices], 
                  color='#512e5f', s=20, label='Checkpoints', zorder=4)
    ax_ps.scatter([psi_gr[0]], [p_gr[0]], [time_steps[0]], color='blue', s=40, label='Initial State', zorder=5)
    ax_ps.scatter([psi_gr[-1]], [p_gr[-1]], [time_steps[-1]], color='black', s=40, label='Final State', zorder=5)
    
    ax_ps.set_title("TOE/GUT: Conjugate Spacetime Manifold", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel("psi_gr", fontsize=8, labelpad=5)
    ax_ps.set_ylabel("p_gr", fontsize=8, labelpad=5)
    ax_ps.set_zlabel("Time", fontsize=8, labelpad=5)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper left', fontsize=7)
    
    ps_file = f"{output_dir}/phase_space_trajectory.png"
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. Multi-Panel Conjugate Coupling Dynamics (Square)
    fig_2d, (ax1, ax2) = plt.subplots(2, 1, figsize=(square_size, square_size), sharex=True)
    
    ax1.plot(time_steps, psi_gr, color='#2980b9', linewidth=1.4, label='GR Perturbation psi_gr')
    ax1.plot(time_steps, q_real, color='#27ae60', linewidth=1.4, linestyle='--', label='QM Real Re(psi_qm)')
    ax1.set_ylabel("Amplitude Field", fontsize=8, fontweight='bold')
    ax1.set_title("TOE/GUT Conjugate Field Interactions", fontsize=9, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.tick_params(axis='both', labelsize=7)
    ax1.legend(loc='upper left', fontsize=7)

    ax2.plot(time_steps, p_gr, color='#c0392b', linewidth=1.4, label='GR Momentum p_gr')
    ax2.plot(time_steps, q_imag, color='#d35400', linewidth=1.4, linestyle='--', label='QM Imaginary Im(psi_qm)')
    ax2.set_xlabel("Normalized Time", fontsize=8, fontweight='bold')
    ax2.set_ylabel("Momentum / Field", fontsize=8, fontweight='bold')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.tick_params(axis='both', labelsize=7)
    ax2.legend(loc='upper left', fontsize=7)

    ts_file = f"{output_dir}/system_evolution.png"
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    print(f"Exported standardized TOE/GUT square plots: {ps_file}, {ts_file}")