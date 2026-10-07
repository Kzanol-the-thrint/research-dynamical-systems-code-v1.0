# sdc_solver.py
import numpy as np

def run_sdc_solver(matrix_map, initial_state, total_days=400.0, dt=0.005):
    """
    Autonomous SDC Matrix Engine. 
    Executes precise tensor propagation using state-dependent operator evaluation.
    """
    steps = int(total_days / dt)
    Phi_state = np.array(initial_state, dtype=np.float64)
    
    trajectory = np.zeros((steps, 3), dtype=np.float64)

    for i in range(steps):
        x, y, z = Phi_state
        
        # Evaluate 3x3 operator cells dynamically based on current state [x, y, z]
        A_num = np.zeros((3, 3), dtype=np.float64)
        for r in range(3):
            for c in range(3):
                A_num[r, c] = matrix_map[r, c](x, y, z)
        
        # Euler step with time increment integration: x(t+dt) = x(t) + A(x)x * dt
        #Phi_state = Phi_state + np.dot(A_num, Phi_state) * dt
        Phi_state =  Phi_state+np.dot(A_num, Phi_state) *dt 
        
        trajectory[i] = Phi_state.copy()

    return trajectory, steps