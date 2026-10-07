import numpy as np

def create_sdc_matrix(params):
    """
    Constructs the N x N SDC Matrix Operator for the Van der Pol Oscillator.
    Equation: x_ddot - mu*(1 - x^2)*x_dot + x = 0
    State 0 (x): position
    State 1 (v): velocity
    """
    mu = params.get("param_1", 2.0)
    dt = params.get("dt", 0.05)

    return np.array([
        # Row 0 (Position Equation): x_next = x + v * dt
        [lambda x0, x1, x2: 1.0,
         lambda x0, x1, x2: dt,
         lambda x0, x1, x2: 0.0],

        # Row 1 (Velocity Equation): v_next = v + [mu*(1 - x^2)*v - x] * dt
        [lambda x0, x1, x2: -dt,
         lambda x0, x1, x2: 1.0 + mu * (1.0 - x0**2) * dt,
         lambda x0, x1, x2: 0.0],

        # Row 2 (Null/Padding for 3D universal pipeline structure)
        [lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 1.0]
    ], dtype=object)