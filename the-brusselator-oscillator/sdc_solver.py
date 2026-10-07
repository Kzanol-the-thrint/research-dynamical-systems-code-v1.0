import numpy as np
from matrix import create_sdc_matrix

class SDCSolver:
    """
    State-Dependent Coefficient (SDC) Matrix Solver Engine for Non-Linear Dynamical Systems.
    """
    def __init__(self, params):
        self.params = params
        self.dt = params.get("dt", 0.01)
        self.horizon = params.get("horizon", 40.0)
        self.steps = int(self.horizon / self.dt)
        
        # Initialize state vector [x0, x1, x2]
        self.state = np.array([
            params.get("x0", 1.5),
            params.get("x1", 0.5),
            params.get("x2", 1.0)
        ], dtype=float)

    def step(self):
        """
        Performs a single SDC matrix-vector integration step: X_next = A(X) * X
        """
        x0, x1, x2 = self.state
        A_func_matrix = create_sdc_matrix(self.params)
        
        # Evaluate lambdas at the current state vector
        A_evaluated = np.zeros((3, 3), dtype=float)
        for i in range(3):
            for j in range(3):
                A_evaluated[i, j] = A_func_matrix[i, j](x0, x1, x2)
                
        # Advance state vector via SDC mapping
        self.state = np.dot(A_evaluated, self.state)

    def run_simulation(self):
        """
        Runs the full temporal simulation across the configured horizon.
        """
        trajectory = [self.state.copy()]
        for _ in range(self.steps):
            self.step()
            trajectory.append(self.state.copy())
            
        return np.array(trajectory)