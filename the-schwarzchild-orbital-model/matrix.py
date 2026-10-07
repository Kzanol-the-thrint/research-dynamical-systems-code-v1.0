import numpy as np

def create_sdc_matrix(M, G, c):
    """
    Constructs the State-Dependent Coefficient (SDC) Matrix for Schwarzschild Relativistic Orbits.
    Maps geodesic equations of motion into autonomous matrix form: X_dot = A(X) * X.
    """
    rs = 2.0 * G * M / (c**2) # Schwarzschild radius
    
    return np.array([
        # Row 0: dr/dt = r_dot
        [lambda r, phi, rd, phd: 0.0,
         lambda r, phi, rd, phd: 0.0,
         lambda r, phi, rd, phd: 1.0,
         lambda r, phi, rd, phd: 0.0],
         
        # Row 1: d(phi)/dt = phi_dot
        [lambda r, phi, rd, phd: 0.0,
         lambda r, phi, rd, phd: 0.0,
         lambda r, phi, rd, phd: 0.0,
         lambda r, phi, rd, phd: 1.0],
         
        # Row 2: Radial geodesic acceleration with 1PN / Schwarzschild correction
        [lambda r, phi, rd, phd: - (G * M / (r**3)) * (1.0 - 3.0 * rs / r) + (phd**2),
         lambda r, phi, rd, phd: 0.0,
         lambda r, phi, rd, phd: 0.0,
         lambda r, phi, rd, phd: 0.0],
         
        # Row 3: Angular acceleration (Coriolis / angular momentum coupling)
        [lambda r, phi, rd, phd: -2.0 * rd * phd / (r**2),
         lambda r, phi, rd, phd: 0.0,
         lambda r, phi, rd, phd: 0.0,
         lambda r, phi, rd, phd: 0.0]
    ], dtype=object)