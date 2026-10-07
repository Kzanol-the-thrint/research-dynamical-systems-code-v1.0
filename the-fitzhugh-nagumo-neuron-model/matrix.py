import numpy as np

def create_sdc_matrix(params):
    """
    Constructs the N x N SDC Matrix Operator for the FitzHugh-Nagumo Neuron Model.
    """
    a = params.get("param_a", 0.7)
    b = params.get("param_b", 0.8)
    c = params.get("param_c", 0.08)
    I = params.get("external_i", 0.5)
    dt = params.get("dt", 0.05)

    return np.array([
        # Row 0: Equation for x0 (Membrane Voltage v)
        [lambda x0, x1, x2: 1.0 + (1.0 - (x0**2) / 3.0) * dt,
         lambda x0, x1, x2: -1.0 * dt,
         lambda x0, x1, x2: I * dt],

        # Row 1: Equation for x1 (Recovery Variable w)
        [lambda x0, x1, x2: c * dt,
         lambda x0, x1, x2: 1.0 - (c * b) * dt,
         lambda x0, x1, x2: (c * a) * dt],

        # Row 2: Constant Anchor x2 = 1.0
        [lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 1.0]
    ], dtype=object)