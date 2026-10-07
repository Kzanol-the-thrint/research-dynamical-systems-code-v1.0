# FLRW Cosmological State-Dependent Coefficient (SDC) Analysis Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

This repository contains the numerical simulation framework accompanying the article:
> **"[Insert Article Title Here]"**  
> *[Author Names]*

The framework implements a State-Dependent Coefficient (SDC) matrix representation to solve the Friedmann–Lemaître–Robertson–Walker (FLRW) cosmological equations across **17 distinct cosmological models**, tracking scale factor evolution $a(t)$ and expansion velocity $\dot{a}(t)$ over cosmic time.

---

## Repository Structure

```text
sdcm-applications-analysis/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
│
├── models/                  # Configurations and parameter sets for all 17 models
│   ├── model_01.py
│   ├── model_02.py
│   └── ...
├── src/                     # Core numerical engine
│   ├── __init__.py
│   ├── matrix.py            # SDC coefficient builder
│   ├── sdc_solver.py        # Symplectic/Euler SDC integration solver
│   └── visualizer.py        # Phase-space and time-evolution renderers
│
└── outputs/                 # Generated trajectory CSVs and standardized figures


Installation
Clone the repository:

Bash
git clone [https://github.com/Kzanol-the-thrint/dynamical_systems.git](https://github.com/Kzanol-the-thrint/dynamical_systems.git)
cd dynamical_systems/sdcm-applications-analysis
Install dependencies:

Bash
pip install -r requirements.txt
Reproducing Results
To run a simulation for a specific model configuration and generate the phase-space manifold and time-evolution plots:

Bash
python main.py --model 1
Generated outputs will include:

phase_space_trajectory.png: 3D phase-space visualization.

system_evolution.png: 2D scale factor and expansion rate subplots.

output_flrw_data.csv: High-resolution numerical export of the trajectory.

Citation
If you use this code or data in your research, please cite our article:

Code snippet
@article{kapadia2026flrw,
  title={...},
  author={Kapadia, Sagar and ...},
  journal={...},
  year={2026}
}