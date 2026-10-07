import numpy as np

# Universal Constants
G = 6.67430e-11
C_LIGHT = 2.99792458e8

def create_sdc_matrix(m1, m2, m3, dt):
    """
    Constructs the 6x6 SDC Matrix Operator for the Post-Newtonian (1PN) Three-Body System.
    Evaluates both Newtonian inverse-cube gravity and 1PN relativistic velocity/potential corrections.
    """
    c2 = C_LIGHT ** 2

    return np.array([
        # Row 0: Separation Distance r12 Evolution (dr12 = p12/m1 * dt)
        [lambda r12, r23, r31, p12, p23, p31: 1.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1 / m1,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0],

        # Row 1: Separation Distance r23 Evolution (dr23 = p23/m2 * dt)
        [lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1 / m2,
         lambda r12, r23, r31, p12, p23, p31: 0.0],

        # Row 2: Separation Distance r31 Evolution (dr31 = p31/m3 * dt)
        [lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1 / m3],

        # Row 3: Momentum p12 Evolution (Newtonian + 1PN Relativistic Correction)
        [lambda r12, r23, r31, p12, p23, p31: - (G * m1 * m2 / (r12**3)) * (1.0 + (3.0 / (c2 * r12)) * ((p12/m1)**2)),
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0],

        # Row 4: Momentum p23 Evolution (Newtonian + 1PN Relativistic Correction)
        [lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: - (G * m2 * m3 / (r23**3)) * (1.0 + (3.0 / (c2 * r23)) * ((p23/m2)**2)),
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0],

        # Row 5: Momentum p31 Evolution (Newtonian + 1PN Relativistic Correction)
        [lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: - (G * m3 * m1 / (r31**3)) * (1.0 + (3.0 / (c2 * r31)) * ((p31/m3)**2)),
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 0.0,
         lambda r12, r23, r31, p12, p23, p31: 1.0]
    ], dtype=object)