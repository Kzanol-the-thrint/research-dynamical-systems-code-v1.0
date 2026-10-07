import numpy as np

def run_sdc_solver(matrix_map, initial_state, total_steps, dt):
    """
    Executes the State-Dependent Coefficient (SDC) discrete solver loop.
    Evaluates matrix lambda functions dynamically at each state vector step.
    """
    dim = len(initial_state)
    trajectory = [np.array(initial_state, dtype=float)]
    
    Phi_state = np.array(initial_state, dtype=float)
    
    # Determine the number of discrete steps based on horizon / dt
    steps = int(total_steps / dt)
    
    for _ in range(steps):
        x0, x1, x2 = Phi_state[0], Phi_state[1], Phi_state[2]
        
        # Dynamically evaluate lambda cells for the current state vector position
        A_num = np.zeros((dim, dim), dtype=float)
        for i in range(dim):
            for j in range(dim):
                cell_func = matrix_map[i, j]
                A_num[i, j] = cell_func(x0, x1, x2)
                
        # Discrete state evolution step: Phi_{next} = A(Phi) * Phi
        Phi_next = np.dot(A_num, Phi_state)
        
        trajectory.append(Phi_next.copy())
        Phi_state = Phi_next
        
    return np.array(trajectory), steps