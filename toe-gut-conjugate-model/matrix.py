import numpy as np

def create_sdc_matrix(state, lam):
    """
    Constructs the 4x4 SDC Matrix for the Combined Conjugate Model.
    State vector: [psi_gr, p_gr, psi_qm_real, psi_qm_imag]
    Couples macroscopic spacetime curvature perturbations with quantum wavefunction dynamics.
    """
    psi_gr, p_gr, q_real, q_imag = state
    
    # Quantum density feedback onto spacetime
    qm_density = (q_real**2) + (q_imag**2)
    
    # Effective curvature frequency modulated by quantum density
    omega_gr_sq = 1.0 + lam * qm_density
    
    # Effective quantum potential modulated by spacetime curvature perturbation
    v_qm = 0.5 + lam * psi_gr

    return np.array([
        # Row 0: d(psi_gr)/dt = p_gr
        [lambda s: 0.0, lambda s: 1.0, lambda s: 0.0, lambda s: 0.0],
        
        # Row 1: d(p_gr)/dt = -omega_gr_sq * psi_gr (Feedback from QM density)
        [lambda s: -omega_gr_sq, lambda s: 0.0, lambda s: -lam * s[2], lambda s: -lam * s[3]],
        
        # Row 2: d(Re_qm)/dt = v_qm * Im_qm (Feedback from GR curvature)
        [lambda s: 0.0, lambda s: 0.0, lambda s: 0.0, lambda s: v_qm],
        
        # Row 3: d(Im_qm)/dt = -v_qm * Re_qm
        [lambda s: 0.0, lambda s: 0.0, lambda s: -v_qm, lambda s: 0.0]
    ], dtype=object)