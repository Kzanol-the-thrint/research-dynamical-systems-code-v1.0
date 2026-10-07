import numpy as np
from matrix import create_sdc_matrix

def run_solver(initial_state, steps, dt, v0, g):
    """
    Executes the SDC matrix differential solver for the Gross-Pitaevskii equation.
    """
    trajectory = [np.array(initial_state, dtype=float)]
    state = np.array(initial_state, dtype=float)

    for _ in range(steps):
        r, im = state[0], state[1]
        
        # Construct SDC matrix A(x)
        A = create_sdc_matrix(r, im, v0, g)
        
        # Evaluate linear-in-state form: dot{x} = A(x) * x
        # Row 0: 0*r + (v0 + g*density)*im
        # Row 1: -(v0 + g*density)*r + 0*im
        d_real = A[0, 1](r, im) * im
        d_imag = A[1, 0](r, im) * r
        
        derivs = np.array([d_real, d_imag], dtype=float)
        
        # 4th Order Runge-Kutta Integration for high stability
        k1 = derivs
        
        r2, im2 = state + 0.5 * dt * k1
        A2 = create_sdc_matrix(r2, im2, v0, g)
        k2 = np.array([A2[0, 1](r2, im2) * im2, A2[1, 0](r2, im2) * r2])
        
        r3, im3 = state + 0.5 * dt * k2
        A3 = create_sdc_matrix(r3, im3, v0, g)
        k3 = np.array([A3[0, 1](r3, im3) * im3, A3[1, 0](r3, im3) * r3])
        
        r4, im4 = state + dt * k3
        A4 = create_sdc_matrix(r4, im4, v0, g)
        k4 = np.array([A4[0, 1](r4, im4) * im4, A4[1, 0](r4, im4) * r4])
        
        state += (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        trajectory.append(state.copy())
        
    return np.array(trajectory)