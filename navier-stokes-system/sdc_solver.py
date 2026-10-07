import numpy as np
from matrix import R

def run_sdc_solver(matrix, day0_obs, target_days=7, N=50, dt=10):
    """
    Autonomous SDC Matrix Engine.
    """
    steps = int((target_days * 86400) / dt)
    spatial_index = np.arange(N, dtype=np.int64)
    
    U_real  = day0_obs["u"]  + ((spatial_index % 5) - 2) * 10
    V_real  = day0_obs["v"]  + ((spatial_index % 3) - 1) * 10
    W_real  = -(R(U_real) - U_real) - (R(V_real) - V_real)
    th_real = day0_obs["th"] + ((spatial_index % 4) - 2) * 5
    m_real  = day0_obs["m"]  + ((spatial_index % 6) - 3) * 20
    ph_real = np.full(N, 985000, dtype=np.int64) + (spatial_index % 10) * 100

    Phi_state = np.array([U_real, V_real, W_real, th_real, m_real, ph_real], dtype=np.int64)
    trajectory_int = np.zeros((steps, 6, N), dtype=np.int64)

    for i in range(steps):
        U, V, W, th, m, ph = Phi_state
        A_num = np.zeros((6, 6, N), dtype=np.int64)
        for r in range(6):
            for c in range(6):
                A_num[r, c] = matrix[r, c](U, V, W, th, m, ph)
        
        Phi_next = np.zeros_like(Phi_state, dtype=np.int64)
        for r in range(6):
            for c in range(6):
                Phi_next[r] = Phi_state[c] + np.dot(A_num[r, c], Phi_state[c])
                
        Phi_state = Phi_next.copy()
        trajectory_int[i] = Phi_state.copy()

    trajectory_int[-1] = Phi_state.copy()
    mid_idx = N // 2
    
    return (
        trajectory_int[:, 0, mid_idx],
        trajectory_int[:, 1, mid_idx],
        trajectory_int[:, 2, mid_idx],
        trajectory_int[:, 3, mid_idx],
        trajectory_int[:, 4, mid_idx],
        steps
    )