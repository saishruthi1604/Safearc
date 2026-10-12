# SafeArc
### Predictive Wearable for Preventing Joint Dislocation During Rehabilitation

SafeArc is a software prototype demonstrating a possible workflow for a future rehabilitation wearable. It lets a user enter illustrative joint-angle, movement-speed, and sensor-confidence values, compares them with configurable demo thresholds, and records sample events.

> **Safety note:** This is an educational software demo only. It does not detect or predict real joint dislocations, is not clinically validated, and must not be used to make treatment decisions. Any real safe range must be set by a qualified clinician. The hardware is not yet implemented.

## Current status
- [x] Streamlit software demonstration
- [x] Configurable illustrative movement limits
- [x] Basic caution/out-of-range status logic
- [x] Session event log and CSV export
- [ ] Live IMU sensor integration
- [ ] Hardware wearable and vibration feedback
- [ ] Clinical validation and usability testing

## Features
- Enter a sample joint angle and angular velocity.
- Configure illustrative lower/upper limits and early-warning margin.
- See a simple status assessment.
- Record events and export a CSV log.

## Run locally
1. Install Python 3.10 or newer.
2. Clone or download this repository.
3. (Recommended) Create and activate a virtual environment.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```
6. Open the local URL shown in your terminal.

## Environment variables
No environment variables or API keys are required for this demo.

## Architecture
```text
User-entered demo values
          |
          v
Input validation and threshold configuration
          |
          v
Rule-based illustrative status logic
          |
          +------> Status display
          |
          +------> Session event log ------> CSV export
```

## Planned system architecture
```text
Two IMUs (future hardware)
       |
       v
Sensor calibration and orientation estimation
       |
       v
Clinician-defined personalized limits
       |
       v
Validated movement-risk model (future work)
       |
       +------> Graded vibration feedback (future hardware)
       |
       +------> Event log for clinician review
```

## Sample data and tests
See `sample_data/sample_movements.csv` and `tests/test_risk_logic.py`. The sample values are synthetic and only exercise the demo logic.

## Limitations
- Inputs are manual; there is no live sensor connection.
- Threshold logic is a simple demonstration, not a trained AI model.
- No claims of prediction accuracy or clinical effectiveness are made.
- Sensor fusion, calibration, security, consent, and clinical validation remain future work.

## License
This project is licensed under the MIT License. See `LICENSE`.

## Disclaimer
SafeArc is not a medical device and is not a substitute for professional medical advice, diagnosis, treatment, or rehabilitation supervision.
