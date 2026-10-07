# domain_lotka_volterra.py
import numpy as np

def create_sdc_matrix(alpha, beta, delta, gamma, dt):
    """
    Constructs the 2x2 SDC Matrix Operator for Lotka-Volterra Dynamics.
    Diagonal entries handle state persistence (1.0).
    Off-diagonal entries handle non-linear encounter rates scaled by dt.
    """
    return np.array([
        # Row 0: Prey Population (X) Evolution -> dx = (alpha - beta * y) * x * dt
        [lambda x, y: alpha ,  lambda x, y: -beta * x],
        
        # Row 1: Predator Population (Y) Evolution -> dy = (delta * x - gamma) * y * dt
        [lambda x, y: delta * y ,    lambda x, y: - gamma]
    ], dtype=object)