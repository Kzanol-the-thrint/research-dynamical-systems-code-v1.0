import numpy as np
from matrix import create_sdc_matrix

def run_solver(initial_state, steps, dt, mass, l_mode, c, g, r_radius):
    trajectory = np.zeros((steps, 2), dtype=np.float64)
    phi_state = np.array(initial_state, dtype=np.float64) # [psi, p]
    
    # Fixed radial shell distance for this run
    r = r_radius

    for i in range(steps):
        psi, p = phi_state
        
        matrix_map = create_sdc_matrix(r, mass, l_mode, c, g)
        
        A_num = np.zeros((2, 2), dtype=np.float64)
        for r_idx in range(2):
            for c_idx in range(2):
                A_num[r_idx, c_idx] = matrix_map[r_idx, c_idx](psi, p)
        
        # SDC Step update
        phi_next = phi_state + np.dot(A_num, phi_state) * dt
        phi_state = phi_next.copy()
        trajectory[i] = phi_state.copy()

    return trajectory