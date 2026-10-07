# sdc_solver.py
import numpy as np

def run_sdc_solver(matrix_map, initial_state, total_time=50.0, dt=0.01):
    """
    Autonomous SDC Matrix Engine for 2-State Ecological Systems.
    """
    steps = int(total_time / dt)
    Phi_state = np.array(initial_state, dtype=np.float64)
    
    trajectory = np.zeros((steps, 2), dtype=np.float64)

    for i in range(steps):
        x, y = Phi_state
        
        # Evaluate operator cells dynamically based on current states x and y
        A_num = np.zeros((2, 2), dtype=np.float64)
        for r in range(2):
            for c in range(2):
                A_num[r, c] = matrix_map[r, c](x, y)
        
        # Advance state vector: Phi_next = A_num dot Phi_state
        #Phi_next = Phi_state + np.dot(A_num, Phi_state)*dt
        Phi_next = Phi_state + np.dot(A_num, Phi_state)*dt
        Phi_state = Phi_next.copy()
        trajectory[i] = Phi_state.copy()

    return trajectory, steps