import matplotlib.pyplot as plt
import numpy as np

def render_plots_and_tables(output_dir, u_phys, v_phys, th_phys, target_dates, daily_indices, param_config, observed_data, target_days):
    # Perfect Square Dimensions for A4 layout harmony (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. Extract the discrete daily checkpoints (Days 1 to 30)
    u_daily = [u_phys[idx] for idx in daily_indices]
    v_daily = [v_phys[idx] for idx in daily_indices]
    th_daily = [th_phys[idx] for idx in daily_indices]

    # Prepend the true Day 0 starting scalar node so the line originates from the blue dot
    u_plot_line  = [u_phys[0]] + u_daily
    v_plot_line  = [v_phys[0]] + v_daily
    th_plot_line = [th_phys[0]] + th_daily

    # 3D Phase-Space Trajectory Rendering (Square)
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111, projection='3d')
    
    # Plot the clean continuous line starting explicitly from Day 0
    ax_ps.plot(u_plot_line, v_plot_line, th_plot_line, color='#1f77b4', lw=1.5, alpha=0.85, label='SDCMS Trajectory')
    
    # Anchor markers
    ax_ps.scatter([u_plot_line[0]], [v_plot_line[0]], [th_plot_line[0]], color='blue', s=40, depthshade=False, label='Day 0 Start')
    ax_ps.scatter(u_daily[-1], v_daily[-1], th_daily[-1], color='red', s=40, depthshade=False, label=f'Day {target_days} End')

    ax_ps.set_title("3D Phase-Space Attractor Trajectory", fontsize=10, pad=4)
    ax_ps.set_xlabel("U Wind Speed (m/s)", fontsize=8, labelpad=2)
    ax_ps.set_ylabel("V Wind Speed (m/s)", fontsize=8, labelpad=2)
    ax_ps.set_zlabel("Temperature (°C)", fontsize=8, labelpad=2)
    ax_ps.tick_params(axis='both', which='major', labelsize=7)
    ax_ps.legend(loc='upper left', fontsize=7, framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/phase_space_attractor.png", dpi=300, bbox_inches='tight')
    plt.close()