# matrix.py
import numpy as np

def create_sdc_matrix(sigma, rho, beta, dt):
    """
    State-Dependent Coefficient (SDC) Matrix Operator for the Lorenz System.
    Factorization 2: Column-Shift Formulation.
    """
    return np.array([
        # Row 1 (x-Equation)
        [lambda x, y, z: -sigma,  lambda x, y, z: sigma,  lambda x, y, z: 0.0],
        
        # Row 2 (y-Equation)
        [lambda x, y, z: rho,     lambda x, y, z: -1.0,   lambda x, y, z: -x],
        
        # Row 3 (z-Equation): Shifted to column 2 (0*x + x*y - beta*z)
        [lambda x, y, z: 0.0,     lambda x, y, z: x,      lambda x, y, z: -beta]
    ], dtype=object)