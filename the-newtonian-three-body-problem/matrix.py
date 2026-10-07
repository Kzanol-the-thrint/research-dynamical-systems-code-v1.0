# matrix.py
import numpy as np

# Universal Gravitational Constant (m^3 kg^-1 s^-2)
G = 6.67430e-11

def create_sdc_matrix(m1, m2, m3, dt):
    """
    Constructs the 6x6 SDC Matrix Operator using canonical conjugate variables (r, p)
    with temporal discretization factor dt integrated into transition rates: A(x) = I + dt * J(x).
    """
    return np.array([
        # Row 0: Separation Distance r12 Evolution (dr12 = p12/m1 * dt)
        [lambda r12, r23, r31, p12, p23, p31: 1.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: dt / m1,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0],

        # Row 1: Separation Distance r23 Evolution (dr23 = p23/m2 * dt)
        [lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: dt / m2,
         lambda r12, r23, r31, p12, p23, p31: 0.0],

        # Row 2: Separation Distance r31 Evolution (dr31 = p31/m3 * dt)
        [lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: dt / m3],

        # Row 3: Momentum p12 Evolution (dp12 = - G*m1*m2/r12^2 * dt)
        [lambda r12, r23, r31, p12, p23, p31: - (G * m1 * m2 / (r12**3)) * dt,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0],

        # Row 4: Momentum p23 Evolution (dp23 = - G*m2*m3/r23^2 * dt)
        [lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: - (G * m2 * m3 / (r23**3)) * dt,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0],

        # Row 5: Momentum p31 Evolution (dp31 = - G*m3*m1/r31^2 * dt)
        [lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: - (G * m3 * m1 / (r31**3)) * dt,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1.0]
    ], dtype=object)