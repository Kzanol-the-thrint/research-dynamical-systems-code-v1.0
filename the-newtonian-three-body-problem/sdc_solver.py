# sdc_solver.py
import numpy as np

def run_sdc_solver(matrix_map, initial_state, total_days=365.0, dt=300.0):
    """
    Autonomous SDC Matrix Engine.
    Executes iterative tensor propagation over the forecast horizon.
    """
    steps = int((total_days * 86400) / dt)
    Phi_state = np.array(initial_state, dtype=np.float64)
    
    trajectory = np.zeros((steps, 6), dtype=np.float64)

    for i in range(steps):
        r12, r23, r31, p12, p23, p31 = Phi_state
        
        # Evaluate operator cells dynamically based on current state vector
        A_num = np.zeros((6, 6), dtype=np.float64)
        for r in range(6):
            for c in range(6):
                A_num[r, c] = matrix_map[r, c](r12, r23, r31, p12, p23, p31)
        
        # Advance state vector: Phi_next = A_num * Phi_state
        Phi_next = np.dot(A_num, Phi_state)
        Phi_state = Phi_next.copy()
        trajectory[i] = Phi_state.copy()

    return trajectory, steps