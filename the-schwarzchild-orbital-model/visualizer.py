import os
import matplotlib.pyplot as plt
import numpy as np

def render_orbital_plots(output_dir, trajectory, dt=1.0):
    """
    Renders 3D Phase-Space Manifold and 2D System Evolution plots for the 
    Schwarzschild Relativistic Orbital model, adhering to standardized square dimensions.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    steps = len(trajectory)
    time_steps = np.arange(steps) * dt
    
    r = trajectory[:, 0]
    phi = trajectory[:, 1]
    rd = trajectory[:, 2]
    phd = trajectory[:, 3]
    
    # Cartesian coordinates for spatial trajectory/manifold mapping
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    checkpoint_count = min(20, steps)
    checkpoint_indices = np.linspace(0, steps - 1, checkpoint_count, dtype=int)

    # Perfect Square Dimensions: Equal width and height (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. 3D Phase-Space Manifold (X Position, Y Position, Time / Radial Velocity)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111, projection='3d')
    
    ax_ps.plot(x, y, time_steps, color='#16a085', linewidth=1.2, label='Relativistic Trajectory')
    ax_ps.scatter(x[checkpoint_indices], y[checkpoint_indices], time_steps[checkpoint_indices], 
                  color='#117a65', s=20, label='Checkpoints', zorder=4)
    ax_ps.scatter([x[0]], [y[0]], [time_steps[0]], color='blue', s=40, label='Initial State', zorder=5)
    ax_ps.scatter([x[-1]], [y[-1]], [time_steps[-1]], color='black', s=40, label='Final State', zorder=5)
    
    ax_ps.set_title("3D Schwarzschild Orbital Phase-Space Manifold", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel(r"X Position (m)", fontsize=8, labelpad=5)
    ax_ps.set_ylabel(r"Y Position (m)", fontsize=8, labelpad=5)
    ax_ps.set_zlabel("Time Steps (s)", fontsize=8, labelpad=5)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper left', fontsize=7)
    
    ps_file = os.path.join(output_dir, "phase_space_trajectory.png")
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. 2D System Evolution Subplots (Square)
    fig_2d, (ax1, ax2) = plt.subplots(2, 1, figsize=(square_size, square_size), sharex=True)
    
    ax1.plot(time_steps, r, color='#2980b9', linewidth=1.4, label=r'Radial Distance $r(t)$')
    ax1.set_ylabel("Radius (m)", fontsize=8, fontweight='bold')
    ax1.set_title("Schwarzschild Orbital System Evolution", fontsize=9, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.tick_params(axis='both', labelsize=7)
    ax1.legend(loc='upper left', fontsize=7)

    ax2.plot(time_steps, rd, color='#e67e22', linewidth=1.4, label=r'Radial Velocity $\dot{r}(t)$')
    ax2.set_xlabel("Time (s)", fontsize=8, fontweight='bold')
    ax2.set_ylabel("Velocity (m/s)", fontsize=8, fontweight='bold')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.tick_params(axis='both', labelsize=7)
    ax2.legend(loc='upper left', fontsize=7)

    ts_file = os.path.join(output_dir, "system_evolution.png")
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    
    print(f"Exported standardized Schwarzschild square plots: {ps_file}, {ts_file}")