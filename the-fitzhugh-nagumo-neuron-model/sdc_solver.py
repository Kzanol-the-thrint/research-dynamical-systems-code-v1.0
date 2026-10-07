import numpy as np
from matrix import create_sdc_matrix

class SDCSolver:
    def __init__(self, params):
        self.params = params
        self.dt = params.get("dt", 0.05)
        self.horizon = params.get("horizon", 100.0)
        self.steps = int(self.horizon / self.dt)
        
        self.state = np.array([
            params.get("x0", -1.0),
            params.get("x1", 1.0),
            params.get("x2", 1.0)
        ], dtype=float)

    def step(self):
        x0, x1, x2 = self.state
        A_func_matrix = create_sdc_matrix(self.params)
        
        A_evaluated = np.zeros((3, 3), dtype=float)
        for i in range(3):
            for j in range(3):
                A_evaluated[i, j] = A_func_matrix[i, j](x0, x1, x2)
                
        self.state = np.dot(A_evaluated, self.state)

    def run_simulation(self):
        trajectory = [self.state.copy()]
        for _ in range(self.steps):
            self.step()
            trajectory.append(self.state.copy())
            
        return np.array(trajectory)