import os
import matplotlib.pyplot as plt
import numpy as np

def render_plots(trajectory, dt, total_time, output_dir="."):
    """
    Renders Phase-Space orbital loops and 2D System Evolution plots as 
    perfect equal-sized squares fitting the portrait A4 layout.
    """
    steps = len(trajectory)
    time_axis = np.arange(steps) * dt
    
    x_prey = trajectory[:, 0]
    y_predator = trajectory[:, 1]
    
    # Perfect Square Dimensions: Equal width and height (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. Phase-Space Trajectory (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111)
    
    ax_ps.plot(x_prey, y_predator, color='#e74c3c', linewidth=1.2, label='Phase Orbit')
    ax_ps.scatter([x_prey[0]], [y_predator[0]], color='blue', s=40, label='Initial State', zorder=5)
    ax_ps.scatter([x_prey[-1]], [y_predator[-1]], color='black', s=40, label='Final State', zorder=5)
    
    ax_ps.set_title("Lotka-Volterra Phase-Space Attractor", fontsize=9, fontweight='bold')
    ax_ps.set_xlabel("Prey Population ($X$)", fontsize=8, labelpad=5)
    ax_ps.set_ylabel("Predator Population ($Y$)", fontsize=8, labelpad=5)
    ax_ps.grid(True, linestyle='--', alpha=0.6)
    ax_ps.tick_params(axis='both', labelsize=7)
    ax_ps.legend(loc='upper right', fontsize=7)
    
    ps_file = os.path.join(output_dir, "phase_space_trajectory.png")
    plt.tight_layout()
    plt.savefig(ps_file, dpi=300)
    plt.close(fig_ps)

    # 2. 2D System Evolution Subplots (Square)
    fig_2d, ax_ts = plt.subplots(figsize=(square_size, square_size))
    
    ax_ts.plot(time_axis, x_prey, color='#2980b9', linewidth=1.4, label='Prey ($X$)')
    ax_ts.plot(time_axis, y_predator, color='#27ae60', linewidth=1.4, label='Predator ($Y$)')
    
    ax_ts.set_title("Prey and Predator Populations Dynamics", fontsize=9, fontweight='bold')
    ax_ts.set_xlabel("Time Units ($t$)", fontsize=8, labelpad=5)
    ax_ts.set_ylabel("Population Count", fontsize=8, labelpad=5)
    ax_ts.grid(True, linestyle='--', alpha=0.6)
    ax_ts.tick_params(axis='both', labelsize=7)
    ax_ts.legend(loc='upper right', fontsize=7)

    ts_file = os.path.join(output_dir, "system_evolution.png")
    plt.tight_layout()
    plt.savefig(ts_file, dpi=300)
    plt.close(fig_2d)
    print(f"Exported standardized Lotka-Volterra square plots: {ps_file}, {ts_file}")


def render_terminal_screenshot(params_dict, initial_dict, steps, x_init, x_final, y_init, y_final, output_dir="."):
    """
    Renders an authentic dark terminal screenshot PNG summarizing execution metrics,
    excluding the OS prompt line.
    """
    alpha = params_dict.get('alpha', 1.0)
    beta = params_dict.get('beta', 0.1)
    delta = params_dict.get('delta', 0.075)
    gamma = params_dict.get('gamma', 1.5)
    
    x0 = initial_dict.get('x0', 10.0)
    y0 = initial_dict.get('y0', 5.0)

    text_content = [
        f"Parameters       : alpha={alpha}, beta={beta}, delta={delta}, gamma={gamma}",
        f"Initial States   : Prey(X)={x0}, Predator(Y)={y0}",
        "====================================================",
        "Exported Phase-Space PNG: ./phase_space_trajectory.png",
        "Exported System Evolution PNG: ./system_evolution.png",
        "Full trajectory written to 'output_lv_trajectory.csv'.",
        "",
        f"Simulation complete over {steps} discrete steps.",
        "----------------------------------------------------",
        f"Prey (X)      : Initial = {x_init:.3f} | Final = {x_final:.3f}",
        f"Predator (Y)  : Initial = {y_init:.3f} | Final = {y_final:.3f}",
        "----------------------------------------------------"
    ]
    
    num_lines = len(text_content)
    max_len = max(len(line) for line in text_content)
    
    fig = plt.figure(figsize=(max_len * 0.105 + 0.4, num_lines * 0.28 + 0.4), facecolor='#1e1e1e')
    ax = fig.add_axes([0.04, 0.04, 0.92, 0.92], facecolor='#1e1e1e')
    ax.axis('off')
    
    y_start = 0.96
    line_spacing = 1.0 / (num_lines + 0.5)
    
    for idx, line in enumerate(text_content):
        y = y_start - (idx * line_spacing)
        
        if "===" in line or "---" in line:
            color = '#666666'
        elif "Simulation complete" in line:
            color = '#ffffff'
        else:
            color = '#cccccc'
            
        ax.text(0.0, y, line, transform=ax.transAxes,
                color=color, fontfamily='monospace', fontsize=10.5,
                verticalalignment='top')
                
    output_file = os.path.join(output_dir, "lv_terminal_screenshot.png")
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='#1e1e1e', edgecolor='none')
    plt.close(fig)
    print(f"Exported Terminal Screenshot PNG: {output_file}")