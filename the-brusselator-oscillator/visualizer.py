import matplotlib.pyplot as plt
import numpy as np

def render_plots(trajectory, time_steps, output_dir="."):
    """
    Renders Phase-Space limit cycle and 2D System Evolution plots for the Brusselator as 
    perfect equal-sized squares fitting the portrait A4 layout.
    """
    x0 = trajectory[:, 0]
    x1 = trajectory[:, 1]
    
    # Perfect Square Dimensions: Equal width and height (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. Phase-Space Trajectory (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111)
    
    ax_ps.plot(x0, x1, color='crimson', lw=1.2, label="SDC Limit Cycle")
    ax_ps.scatter([x0[0]], [x1[0]], color='blue', s=40, zorder=5, label="Initial State")
    ax_ps.scatter([x0[-1]], [x1[-1]], color='black', s=40, zorder=5, label="Final State")
    
    ax_ps.set_title("Brusselator Chemical Oscillator Phase-Space", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel("Chemical X ($x_0$)", fontsize=8, labelpad=5)
    ax_ps.set_ylabel("Chemical Y ($x_1$)", fontsize=8, labelpad=5)
    ax_ps.grid(True, linestyle='--', alpha=0.6)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper right', fontsize=7)
    
    ps_file = f"{output_dir}/phase_space_trajectory.png"
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. System Evolution Subplots (Square)
    fig_2d, ax_ts = plt.subplots(figsize=(square_size, square_size))
    
    ax_ts.plot(time_steps, x0, color='tab:blue', lw=1.4, label="Chemical X ($x_0$)")
    ax_ts.plot(time_steps, x1, color='tab:green', lw=1.4, label="Chemical Y ($x_1$)")
    
    ax_ts.set_title("Brusselator Concentrations Over Time", fontsize=9, fontweight='bold')
    ax_ts.set_xlabel("Time Units ($t$)", fontsize=8, labelpad=5)
    ax_ts.set_ylabel("Concentration", fontsize=8, labelpad=5)
    ax_ts.grid(True, linestyle='--', alpha=0.6)
    ax_ts.tick_params(axis='both', labelsize=7)
    ax_ts.legend(loc='upper right', fontsize=7)

    ts_file = f"{output_dir}/system_evolution.png"
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    print(f"Exported standardized Brusselator square plots: {ps_file}, {ts_file}")