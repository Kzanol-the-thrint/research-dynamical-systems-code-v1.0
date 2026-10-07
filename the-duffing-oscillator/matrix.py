import numpy as np

def create_sdc_matrix(params):
    """
    Constructs the N x N SDC Matrix Operator for the Duffing Oscillator.
    Models non-linear spring mechanics with cubic stiffness and periodic driving.
    """
    delta = params.get("param_1", 0.1)      # Damping coefficient
    alpha = -1.0                            # Linear stiffness (negative for double-well)
    beta = params.get("param_2", 1.0)       # Non-linear cubic stiffness
    gamma = params.get("normalization_factor", 0.3) # Driving amplitude
    omega = 1.2                             # Driving frequency
    dt = params.get("dt", 0.05)

    return np.array([
        # Row 0: Equation for x0 (Displacement) -> x0_next = x0 + x1 * dt
        [lambda x0, x1, x2: 1.0,
         lambda x0, x1, x2: dt,
         lambda x0, x1, x2: 0.0],

        # Row 1: Equation for x1 (Velocity) -> includes non-linear cubic term and driving force
        [lambda x0, x1, x2: (alpha + beta * (x0**2)) * dt,
         lambda x0, x1, x2: 1.0 - delta * dt,
         lambda x0, x1, x2: (gamma * np.cos(omega * x2) / (x1 + 1e-9)) * dt],

        # Row 2: Equation for x2 (Time phase) -> x2_next = x2 + 1.0 * dt
        [lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 0.0,
         lambda x0, x1, x2: 1.0]
    ], dtype=object)