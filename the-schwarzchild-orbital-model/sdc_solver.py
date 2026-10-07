import numpy as np

def run_schwarzschild_solver(matrix_map, initial_state, steps=10000, dt=1.0):
    """
    Autonomous State-Dependent Coefficient (SDC) Solver for Relativistic Orbital Mechanics.
    """
    Phi_state = np.array(initial_state, dtype=np.float64)
    trajectory = np.zeros((steps, 4), dtype=np.float64)

    for i in range(steps):
        r, phi, rd, phd = Phi_state
        
        # Prevent gravitational collapse singularity check
        if r <= 3.0 * 1475.0:  
            r = max(r, 1000.0)
            
        A_num = np.zeros((4, 4), dtype=np.float64)
        for r_idx in range(4):
            for c_idx in range(4):
                A_num[r_idx, c_idx] = matrix_map[r_idx, c_idx](r, phi, rd, phd)
        
        # Symplectic SDC Step update
        Phi_next = Phi_state + np.dot(A_num, Phi_state) * dt
        Phi_state = Phi_next.copy()
        trajectory[i] = Phi_state.copy()

    return trajectory, steps