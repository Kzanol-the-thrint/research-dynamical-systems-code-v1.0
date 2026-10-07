import numpy as np
from matrix import create_sdc_matrix

class SDCSolver:
    def __init__(self, params):
        self.params = params
        self.dt = params.get("dt", 0.01)
        self.horizon = params.get("horizon", 200.0)
        self.steps = int(self.horizon / self.dt)
        
        self.state = np.array([
            params.get("x0", 0.1),
            params.get("x1", 0.0),
            params.get("x2", 0.0),
            params.get("x3", 1.0)
        ], dtype=float)

    def step(self):
        x0, x1, x2, x3 = self.state
        A_func_matrix = create_sdc_matrix(self.params)
        
        n = len(self.state)
        A_evaluated = np.zeros((n, n), dtype=float)
        for i in range(n):
            for j in range(n):
                A_evaluated[i, j] = A_func_matrix[i, j](x0, x1, x2, x3)
                
        self.state = np.dot(A_evaluated, self.state)

    def run_simulation(self):
        trajectory = [self.state.copy()]
        for _ in range(self.steps):
            self.step()
            trajectory.append(self.state.copy())
            
        return np.array(trajectory)