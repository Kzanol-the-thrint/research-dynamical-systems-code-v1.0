# matrix.py
import numpy as np

def create_sdc_matrix(sigma, rho, beta, dt):
    """
    State-Dependent Coefficient (SDC) Matrix Operator for the Lorenz System.
    Restructures the non-linear convective ODEs into discrete linear matrix-vector form: 
    x(t+dt) = A(x) * x(t), where A(x) = I + dt * J(x).
    """
    return np.array([
        # Row 1 (x-Equation): x + (-sigma*x + sigma*y)*dt -> (1 - sigma*dt)x + (sigma*dt)y
        [lambda x, y, z:  - sigma ,  lambda x, y, z: sigma ,     lambda x, y, z: 0.0],
        
        # Row 2 (y-Equation): y + (rho*x - y - x*z)*dt -> (rho*dt)x + (1 - dt)y + (-dt*x)z
        [lambda x, y, z: rho ,          lambda x, y, z: 1.0 ,      lambda x, y, z: -x ],
        
        # Row 3 (z-Equation): z + (x*y - beta*z)*dt -> (dt*y)x + 0*y + (1 - beta*dt)z
        [lambda x, y, z: y ,          lambda x, y, z: 0.0,            lambda x, y, z:  - beta ]
    ], dtype=object)