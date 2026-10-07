import numpy as np

def create_sdc_matrix(params):
    """
    Constructs the N x N SDC Matrix Operator for the Oregonator Chemical Oscillator.
    Models the Belousov-Zhabotinsky reaction kinetics.
    """
    q = params.get("param_1", 0.002)
    f = params.get("param_2", 1.0)
    epsilon = params.get("normalization_factor", 0.03)
    dt = params.get("dt", 0.01)

    return np.array([
        # Row 0: Equation for x0 (HBrO2)
        [lambda x0, x1, x2: 1.0 + ((1.0 - x0 - x1) / epsilon) * dt,
         lambda x0, x1, x2: (q / epsilon) * (x1 / (x0 + 1e-9)) * dt,
         lambda x0, x1, x2: 0.0],

        # Row 1: Equation for x1 (Br-)
        [lambda x0, x1, x2: -x1 * dt,
         lambda x0, x1, x2: 1.0 - q * dt,
         lambda x0, x1, x2: f * (x2 / (x1 + 1e-9)) * dt],

        # Row 2: Equation for x2 (Ce4+)
        [lambda x0, x1, x2: (1.0 / (x2 + 1e-9)) * dt,
         lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 1.0 - dt]
    ], dtype=object)