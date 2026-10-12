# Test Plan

| ID | Input | Expected demo result |
|---|---|---|
| T01 | Angle 55°, speed 35°/s, confidence 95% | WITHIN DEMO RANGE |
| T02 | Angle 88°, speed 30°/s, confidence 95% | CAUTION |
| T03 | Angle 110°, speed 40°/s, confidence 95% | OUTSIDE DEMO RANGE |
| T04 | Angle 45°, speed 180°/s, confidence 95% | CAUTION |
| T05 | Angle 50°, speed 30°/s, confidence 20% | CHECK SENSOR |

These tests check software demonstration logic only; they do not validate clinical safety or predictive performance.
