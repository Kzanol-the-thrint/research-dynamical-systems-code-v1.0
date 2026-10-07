import argparse
import numpy as np

def R(arr):
    """
    Standard Shift Operator Matrix.
    Rolls the integer array coordinates by -1 to evaluate discrete differences.
    """
    return np.roll(arr, -1)

def get_config():
    parser = argparse.ArgumentParser(description="Generalized Autonomous SDCMS Core Engine")
    parser.add_argument("--start_date", type=str, default="01-07-2026", help="Initialization Date (DD-MM-YYYY)")
    parser.add_argument("--horizon", type=int, default=30, help="Forecast horizon in elapsed days")
    parser.add_argument("--input_file", type=str, default="data/input/data.csv", help="Path to input raw meteorological metrics")
    parser.add_argument("--nodes", type=int, default=50, help="Total number of horizontal grid cells (N)")
    parser.add_argument("--timestep", type=int, default=10, help="Temporal integration step size in seconds (dt)")
    return parser.parse_args()

def create_sdc_matrix(g_i, P_0):
    """
    Pristine State-Dependent Coefficient Matrix Operator.
    """
    return np.array([
        [lambda U,V,W,th,m,ph: np.ones_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: -(R(U*U) - U*U) + (R(W*U) - W*U) + (P_0 - 10*ph)*(R(ph) - ph)],

        [lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.ones_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: -(R(U*V) - U*V) - (R(W*V) - W*V) + (P_0 - 10*ph)*(R(ph) - ph)],

        [lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.ones_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: -(R(U*W) - U*W) + g_i*(R(P_0 - 10*ph) - (P_0 - 10*ph)) - g_i*m,
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64)],

        [lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.ones_like(U, dtype=np.int64) - (R(U) - U),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64)],

        [lambda U,V,W,th,m,ph: -(R(m) - m),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.ones_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64)],

        [lambda U,V,W,th,m,ph: -(R(ph) - ph),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.full_like(U, g_i, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.zeros_like(U, dtype=np.int64),
         lambda U,V,W,th,m,ph: np.ones_like(U, dtype=np.int64)]
    ], dtype=object)

def show_parameters(args):
    print("====================================================")
    print("Initializing SDCMS Pipeline Execution...")
    print(f"Target Origin Anchor : {args.start_date}")
    print(f"Forecast Horizon    : {args.horizon} Days")
    print(f"Grid Space Density  : {args.nodes} Cells")
    print(f"Time Step           : {args.timestep}")
    print(f"Data Substrate Path : {args.input_file}")
    print("====================================================")