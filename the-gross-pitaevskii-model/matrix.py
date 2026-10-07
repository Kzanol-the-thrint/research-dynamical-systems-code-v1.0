import numpy as np

def create_sdc_matrix(psi_real, psi_imag, v0, g):
    """
    Constructs the SDC matrix for the Gross-Pitaevskii Nonlinear Schrödinger Equation.
    State vector: [psi_real, psi_imag] representing the real and imaginary parts 
    of the macroscopic quantum wavefunction psi = psi_real + i * psi_imag[cite: 12].
    
    Governing split field equations[cite: 12]:
    d(psi_real)/dt =  (v0 + g * (psi_real^2 + psi_imag^2)) * psi_imag
    d(psi_imag)/dt = -(v0 + g * (psi_real^2 + psi_imag^2)) * psi_real
    """
    density = (psi_real**2) + (psi_imag**2)
    effective_potential = v0 + (g * density)
    
    # State-Dependent Coefficient (SDC) matrix form: dot{x} = A(x) * x[cite: 12]
    return np.array([
        # Row 0: d(psi_real)/dt coefficients
        [lambda r, im: 0.0, 
         lambda r, im: (v0 + g * (r**2 + im**2))],
         
        # Row 1: d(psi_imag)/dt coefficients
        [lambda r, im: -(v0 + g * (r**2 + im**2)), 
         lambda r, im: 0.0]
    ], dtype=object)