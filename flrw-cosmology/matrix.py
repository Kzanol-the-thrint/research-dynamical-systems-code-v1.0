import numpy as np

def create_sdc_matrix(omega_m, omega_r, omega_l, h0, dt):
    """
    Constructs the State-Dependent Coefficient (SDC) Matrix for FLRW Cosmology.
    State vector: [a, da/dt] representing scale factor and expansion velocity dynamics.
    """
    return np.array([
        # Row 0: Scale factor evolution (da/dt = momentum term pa)
        [lambda a, pa: 0.0, 
         lambda a, pa: 1.0],
         
        # Row 1: Corrected Friedmann acceleration equation mapped into SDC coefficient form
        # a_dot_dot / a = -H0^2 * (omega_r / a^4 + 0.5 * omega_m / a^3 - omega_l)
        [lambda a, pa: - (h0**2) * ((omega_r / (a**4)) + (0.5 * omega_m / (a**3)) - omega_l),
         lambda a, pa: 0.0]
    ], dtype=object)