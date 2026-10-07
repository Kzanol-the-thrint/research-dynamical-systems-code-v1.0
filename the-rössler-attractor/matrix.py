import numpy as np

def create_sdc_matrix(params):
    """
    Constructs the N x N SDC Matrix Operator for the Rössler Attractor.
    """
    a = params.get("param_a", 0.2)
    b = params.get("param_b", 0.2)
    c = params.get("param_c", 5.7)
    dt = params.get("dt", 0.01)

    return np.array([
        # Row 0: Equation for x0 (x) -> x0_dot = -x1 - x2
        [lambda x0, x1, x2, x3: 1.0,
         lambda x0, x1, x2, x3: -dt,
         lambda x0, x1, x2, x3: -dt,
         lambda x0, x1, x2, x3: 0.0],

        # Row 1: Equation for x1 (y) -> x1_dot = x0 + a*x1
        [lambda x0, x1, x2, x3: dt,
         lambda x0, x1, x2, x3: 1.0 + a * dt,
         lambda x0, x1, x2, x3: 0.0,
         lambda x0, x1, x2, x3: 0.0],

        # Row 2: Equation for x2 (z) -> x2_dot = b + z*(x - c)
        [lambda x0, x1, x2, x3: 0.0,
         lambda x0, x1, x2, x3: 0.0,
         lambda x0, x1, x2, x3: 1.0 + (x0 - c) * dt,
         lambda x0, x1, x2, x3: b * dt],

        # Row 3: Constant Anchor x3 = 1.0
        [lambda x0, x1, x2, x3: 0.0,
         lambda x0, x1, x2, x3: 0.0,
         lambda x0, x1, x2, x3: 0.0,
         lambda x0, x1, x2, x3: 1.0]
    ], dtype=object)