DT = 0.005
TOTAL_STEPS = 6000
MASS_Q = 1.0
HBAR = 1.0
POTENTIAL_V0 = 0.5
NONLINEAR_G = 1.2
INPUT_FILE = "input_data.csv"
OUTPUT_FILE = "output_data.csv"

def load_system_data():
    return {
        "psi_real_init": 1.0,
        "psi_imag_init": 0.0
    }