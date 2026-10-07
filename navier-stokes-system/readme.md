# SDCMS (State-Dependent Coefficient Modeling System)

Autonomous meteorological solver engine designed to ingest raw observation records, compute vector components, evaluate state-dependent coefficient matrix operators, and validate forecasts against historical records.

## Usage
Run the main script with default or custom arguments:
```bash
python -m src.main --horizon 30 --nodes 50 --timestep 10