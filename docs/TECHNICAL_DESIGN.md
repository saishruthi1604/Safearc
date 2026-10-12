# SafeArc Technical Design (Prototype)

## Purpose
Demonstrate the software flow for a potential rehabilitation movement monitor using synthetic/manual inputs.

## Components
1. **Input UI:** Streamlit sliders and number inputs.
2. **Threshold configuration:** illustrative lower and upper angles plus warning margin.
3. **Rule-based assessment:** checks input confidence, range boundaries, proximity to limits, and a simple speed threshold.
4. **Event log:** stores recorded values in Streamlit session state.
5. **Export:** downloads the session log as CSV.

## Data flow
```text
Manual sample input -> Rule checks -> Status and explanation -> Event log -> CSV export
```

## Current limitations
No wearable sensor, IMU fusion, predictive machine-learning model, vibration motor, patient account, cloud storage, or clinical validation is implemented. The current rule logic is not medical guidance.
