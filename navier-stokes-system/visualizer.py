import matplotlib.pyplot as plt
import numpy as np

def render_plots_and_tables(output_dir, u_phys, v_phys, w_phys, th_phys, m_phys, target_dates, daily_indices, param_config, observed_data, target_days):
    # Perfect Square Dimensions for A4 layout harmony (~5.26 inches = 90% of half A4 height)
    square_size = (11.6929 * 0.5) * 0.9

    # 1. Extract the discrete daily checkpoints (Days 1 to target_days)
    u_daily  = [u_phys[idx] for idx in daily_indices]
    v_daily  = [v_phys[idx] for idx in daily_indices]
    w_daily  = [w_phys[idx] for idx in daily_indices]
    th_daily = [th_phys[idx] for idx in daily_indices]
    m_daily  = [m_phys[idx] for idx in daily_indices]

    # Prepend the true Day 0 starting scalar node so the line originates from the blue dot
    u_plot_line  = [u_phys[0]] + u_daily
    v_plot_line  = [v_phys[0]] + v_daily
    th_plot_line = [th_phys[0]] + th_daily

    # --- 1. 3D Phase-Space Trajectory Rendering ---
    fig_ps = plt.figure(figsize=(square_size, square_size))
    ax_ps = fig_ps.add_subplot(111, projection='3d')
    
    ax_ps.plot(u_plot_line, v_plot_line, th_plot_line, color='#1f77b4', lw=1.5, alpha=0.85, label='SDCMS Trajectory')
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

    # --- 2. Comprehensive 5-Panel System Evolution Time-Series Plot ---
    fig, axes = plt.subplots(5, 1, figsize=(9, 14), sharex=True)
    
    days_axis = range(1, len(u_daily) + 1)
    
    # Panel 1: U-Wind
    axes[0].plot(days_axis, u_daily, label='Predicted U-Wind', color='#1f77b4', lw=2, marker='o', markersize=3)
    axes[0].plot(days_axis, [obs['u_act'] for obs in observed_data[:len(u_daily)]], label='Actual U-Wind', color='black', linestyle='--', alpha=0.7)
    axes[0].set_ylabel('U-Wind (m/s)', fontsize=9)
    axes[0].set_title('Comprehensive 5-Parameter System Evolution Over Forecast Horizon', fontsize=11, fontweight='bold')
    axes[0].legend(loc='upper right', fontsize=8)
    axes[0].grid(True, linestyle=':', alpha=0.6)

    # Panel 2: V-Wind
    axes[1].plot(days_axis, v_daily, label='Predicted V-Wind', color='#ff7f0e', lw=2, marker='s', markersize=3)
    axes[1].plot(days_axis, [obs['v_act'] for obs in observed_data[:len(v_daily)]], label='Actual V-Wind', color='black', linestyle='--', alpha=0.7)
    axes[1].set_ylabel('V-Wind (m/s)', fontsize=9)
    axes[1].legend(loc='upper right', fontsize=8)
    axes[1].grid(True, linestyle=':', alpha=0.6)

    # Panel 3: W-Wind (Vertical)
    axes[2].plot(days_axis, w_daily, label='Predicted W-Wind', color='#9467bd', lw=2, marker='d', markersize=3)
    axes[2].set_ylabel('W-Wind (m/s)', fontsize=9)
    axes[2].legend(loc='upper right', fontsize=8)
    axes[2].grid(True, linestyle=':', alpha=0.6)

    # Panel 4: Temperature
    axes[3].plot(days_axis, th_daily, label='Predicted Temp', color='#2ca02c', lw=2, marker='^', markersize=3)
    axes[3].plot(days_axis, [obs['temp'] for obs in observed_data[:len(th_daily)]], label='Actual Temp', color='black', linestyle='--', alpha=0.7)
    axes[3].set_ylabel('Temperature (°C)', fontsize=9)
    axes[3].legend(loc='upper right', fontsize=8)
    axes[3].grid(True, linestyle=':', alpha=0.6)

    # Panel 5: Pressure
    axes[4].plot(days_axis, m_daily, label='Predicted Pressure', color='#d62728', lw=2, marker='v', markersize=3)
    axes[4].plot(days_axis, [obs['pressure'] for obs in observed_data[:len(m_daily)]], label='Actual Pressure', color='black', linestyle='--', alpha=0.7)
    axes[4].set_ylabel('Pressure (hPa)', fontsize=9)
    axes[4].set_xlabel('Forecast Day Index', fontsize=9)
    axes[4].legend(loc='upper right', fontsize=8)
    axes[4].grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()
    plt.savefig(f"{output_dir}/system_evolution.png", dpi=300, bbox_inches='tight')
    plt.close()