import matplotlib.pyplot as plt
import numpy as np

def render_plots(trajectory, time_steps, output_dir="."):
    """
    Renders Phase-Space trajectory and 2D System Evolution spike train plots for the FitzHugh-Nagumo model as 
    perfect equal-sized squares fitting the portrait A4 layout.
    """
    v = trajectory[:, 0]
    w = trajectory[:, 1]
    
    # Perfect Square Dimensions: Equal width and height (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. Phase-Space Trajectory (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111)
    
    ax_ps.plot(v, w, color='purple', lw=1.2, label="SDC Neuron Trajectory")
    ax_ps.scatter([v[0]], [w[0]], color='blue', s=40, zorder=5, label="Initial State")
    ax_ps.scatter([v[-1]], [w[-1]], color='black', s=40, zorder=5, label="Final State")
    
    ax_ps.set_title("FitzHugh-Nagumo Phase-Space Trajectory", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel("Membrane Potential ($v$)", fontsize=8, labelpad=5)
    ax_ps.set_ylabel("Recovery Variable ($w$)", fontsize=8, labelpad=5)
    ax_ps.grid(True, linestyle='--', alpha=0.6)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper right', fontsize=7)
    
    ps_file = f"{output_dir}/phase_space_trajectory.png"
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. System Evolution Subplots (Square)
    fig_2d, ax_ts = plt.subplots(figsize=(square_size, square_size))
    
    ax_ts.plot(time_steps, v, color='tab:red', lw=1.4, label="Voltage ($v$)")
    ax_ts.plot(time_steps, w, color='tab:blue', lw=1.4, label="Recovery ($w$)")
    
    ax_ts.set_title("Action Potential Spike Train Over Time", fontsize=9, fontweight='bold')
    ax_ts.set_xlabel("Time Units ($t$)", fontsize=8, labelpad=5)
    ax_ts.set_ylabel("Amplitude", fontsize=8, labelpad=5)
    ax_ts.grid(True, linestyle='--', alpha=0.6)
    ax_ts.tick_params(axis='both', labelsize=7)
    ax_ts.legend(loc='upper right', fontsize=7)

    ts_file = f"{output_dir}/system_evolution.png"
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    print(f"Exported standardized FitzHugh-Nagumo square plots: {ps_file}, {ts_file}")