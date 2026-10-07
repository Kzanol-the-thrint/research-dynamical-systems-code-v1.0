import numpy as np
from matrix import create_sdc_matrix

def run_solver(initial_state, steps, dt, v0, g):
    trajectory = np.zeros((steps, 2), dtype=np.float64)
    state = np.array(initial_state, dtype=np.float64) # [psi_real, psi_imag]

    for i in range(steps):
        r_val, im_val = state
        
        matrix_map = create_sdc_matrix(r_val, im_val, v0, g)
        
        A_num = np.zeros((2, 2), dtype=np.float64)
        for r_idx in range(2):
            for c_idx in range(2):
                A_num[r_idx, c_idx] = matrix_map[r_idx, c_idx](r_val, im_val)
        
        # SDC Step update
        state_next = state + np.dot(A_num, state) * dt
        state = state_next.copy()
        trajectory[i] = state.copy()

    return trajectory