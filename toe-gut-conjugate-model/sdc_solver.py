import numpy as np
from matrix import create_sdc_matrix

def run_solver(initial_state, steps, dt, lam):
    trajectory = np.zeros((steps, 4), dtype=np.float64)
    state = np.array(initial_state, dtype=np.float64) # [psi_gr, p_gr, q_real, q_imag]

    for i in range(steps):
        matrix_map = create_sdc_matrix(state, lam)
        
        A_num = np.zeros((4, 4), dtype=np.float64)
        for r_idx in range(4):
            for c_idx in range(4):
                A_num[r_idx, c_idx] = matrix_map[r_idx, c_idx](state)
        
        # SDC Step update
        state_next = state + np.dot(A_num, state) * dt
        state = state_next.copy()
        trajectory[i] = state.copy()

    return trajectory