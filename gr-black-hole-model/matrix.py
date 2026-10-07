import numpy as np

def create_sdc_matrix(r, mass, l_mode, c, g):
    """
    Constructs the SDC matrix for black hole metric curvature perturbations.
    State vector: [psi, p_psi] where p_psi is the wave amplitude momentum.
    """
    # Schwarzschild radius r_s = 2GM/c^2
    r_s = (2.0 * g * mass) / (c**2)
    
    # Effective Regge-Wheeler potential V_eff(r)
    # Prevent division by zero or negative radius inside horizon
    effective_r = max(r, r_s * 1.001)
    f_factor = (1.0 - (r_s / effective_r))
    v_eff = f_factor * ((l_mode * (l_mode + 1.0) / (effective_r**2)) + (r_s / (effective_r**3)))

    return np.array([
        # Row 0: d(psi)/dt = momentum term
        [lambda psi, p: 0.0, 
         lambda psi, p: 1.0],
         
        # Row 1: d(p_psi)/dt = - V_eff * psi (curvature restoring force)
        [lambda psi, p: -v_eff, 
         lambda psi, p: 0.0]
    ], dtype=object)