# matrix.py
import numpy as np

def create_sdc_matrix(params, dt):
    """
    Constructs the N x N SDC Matrix Operator for the SIR Epidemiological Model.
    """
    beta = params.get("param_1", 0.4)
    gamma = params.get("param_2", 0.1)

    return np.array([
        # Row 0 (S-Equation): S_next = S * (1 - beta * I * dt)
        [lambda x0, x1, x2: 1.0 - beta * x1 * dt,
         lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 0.0],

        # Row 1 (I-Equation): I_next = I * (1 + (beta * S - gamma) * dt)
        [lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 1.0 + (beta * x0 - gamma) * dt,
         lambda x0, x1, x2: 0.0],

        # Row 2 (R-Equation): R_next = R + gamma * I * dt
        [lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: gamma * dt,
         lambda x0, x1, x2: 1.0]
    ], dtype=object)