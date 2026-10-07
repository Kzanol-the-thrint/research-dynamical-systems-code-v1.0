import numpy as np

def create_sdc_matrix(psi_real, psi_imag, v0, g):
    """
    Constructs the SDC matrix for the Nonlinear Schrödinger / Gross-Pitaevskii Equation.
    State vector: [psi_real, psi_imag] representing the real and imaginary parts 
    of the complex quantum wavefunction psi = psi_real + i * psi_imag.
    
    Governing equations (split real/imaginary):
    d(psi_real)/dt = -(1/hbar) * [ -v0 * psi_imag - g * (psi_real^2 + psi_imag^2) * psi_imag ]  (simplified symplectic form)
    d(psi_imag)/dt =  (1/hbar) * [ -v0 * psi_real - g * (psi_real^2 + psi_imag^2) * psi_real ]
    """
    density = (psi_real**2) + (psi_imag**2)
    
    # Effective non-linear coefficient including external potential and self-interaction
    # Notice how the matrix coefficients depend directly on the state vector elements (psi_real, psi_imag),
    # embodying the true State-Dependent Coefficient (SDC) framework!
    
    return np.array([
        # Row 0: d(psi_real)/dt coefficients
        [lambda r, im: 0.0, 
         lambda r, im: (v0 + g * (r**2 + im**2))],
         
        # Row 1: d(psi_imag)/dt coefficients
        [lambda r, im: -(v0 + g * (r**2 + im**2)), 
         lambda r, im: 0.0]
    ], dtype=object)