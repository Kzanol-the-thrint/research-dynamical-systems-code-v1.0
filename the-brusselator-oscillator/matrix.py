import numpy as np

def create_sdc_matrix(params):
    """
    Constructs the N x N SDC Matrix Operator for the Brusselator Chemical Oscillator.
    """
    A = params.get("param_a", 1.0)
    B = params.get("param_b", 3.0)
    dt = params.get("dt", 0.01)

    return np.array([
        # Row 0: Equation for x0 (Chemical X) -> x0_next = x0 + (A - (B+1)*x0 + x0^2*y) * dt
        [lambda x0, x1, x2: 1.0 - (B + 1.0) * dt + x0 * x1 * dt,
         lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: (A * dt) / (x0 + 1e-9)],

        # Row 1: Equation for x1 (Chemical Y) -> x1_next = x1 + (B*x0 - x0^2*y) * dt
        [lambda x0, x1, x2: B * dt - x0 * x1 * dt,
         lambda x0, x1, x2: 1.0,
         lambda x0, x1, x2: 0.0],

        # Row 2: Constant Anchor x2 = 1.0 -> x2_next = x2
        [lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 1.0]
    ], dtype=object)