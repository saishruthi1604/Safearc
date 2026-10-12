import streamlit as st
import math
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SafeArc | Rehab Movement Monitor", page_icon="🛡️", layout="wide")

st.title("🛡️ SafeArc")
st.subheader("Predictive movement-safety prototype for rehabilitation")
st.warning(
    "Prototype/demo only. The values below are manually entered or simulated; this is not a medical device, "
    "does not diagnose or predict real dislocations, and must not guide treatment. Use only with clinical supervision."
)

if "events" not in st.session_state:
    st.session_state.events = []

st.markdown("""
SafeArc is a software demonstration of a future wearable that could use two IMUs to estimate joint movement,
compare it with a clinician-defined safe range, and provide graded feedback when movement approaches a configured limit.
The current demo uses user-entered sample values—not live wearable sensors.
""")

left, right = st.columns(2)
with left:
    st.markdown("### 1. Configure demo thresholds")
    safe_min = st.number_input("Lower demo angle limit (°)", min_value=-180, max_value=180, value=10, step=5)
    safe_max = st.number_input("Upper demo angle limit (°)", min_value=-180, max_value=180, value=90, step=5)
    warning_margin = st.slider("Early-warning margin (°)", min_value=1, max_value=30, value=10)
    st.caption("These are illustrative software settings, not recommended clinical limits.")
with right:
    st.markdown("### 2. Enter a sample movement")
    angle = st.slider("Estimated joint angle (°)", min_value=-180, max_value=180, value=55)
    angular_velocity = st.slider("Angular velocity (°/s)", min_value=0, max_value=300, value=35)
    sensor_confidence = st.slider("Demo sensor confidence (%)", min_value=0, max_value=100, value=95)

if safe_min >= safe_max:
    st.error("The lower limit must be less than the upper limit.")
    st.stop()

distance_to_limit = min(angle - safe_min, safe_max - angle)
outside_range = angle < safe_min or angle > safe_max
near_limit = not outside_range and distance_to_limit <= warning_margin
fast_motion = angular_velocity >= 150

if sensor_confidence < 50:
    status, level, explanation = "CHECK SENSOR", "Data quality", "Demo confidence is low; do not interpret the movement status."
elif outside_range:
    status, level, explanation = "OUTSIDE DEMO RANGE", "High attention", "The entered angle is outside the configured illustrative range."
elif near_limit or fast_motion:
    status, level, explanation = "CAUTION", "Early attention", "The angle is near a configured limit or the entered motion speed is high."
else:
    status, level, explanation = "WITHIN DEMO RANGE", "Low attention", "The entered values are within the configured illustrative range."

st.markdown("### 3. Demo assessment")
a, b, c = st.columns(3)
a.metric("Status", status)
b.metric("Distance to nearest limit", f"{max(0, distance_to_limit):.0f}°" if not outside_range else "Outside")
c.metric("Motion speed", f"{angular_velocity}°/s")
st.info(f"**{level}:** {explanation}")

if st.button("Record demo event", type="primary"):
    st.session_state.events.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "angle_deg": angle,
        "angular_velocity_deg_s": angular_velocity,
        "sensor_confidence_pct": sensor_confidence,
        "status": status
    })
    st.success("Demo event recorded in this browser session.")

st.markdown("### 4. Event log")
if st.session_state.events:
    df = pd.DataFrame(st.session_state.events)
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.download_button("Download event log CSV", df.to_csv(index=False).encode("utf-8"), "safearc_demo_events.csv", "text/csv")
    if st.button("Clear event log"):
        st.session_state.events = []
        st.rerun()
else:
    st.caption("No events recorded yet. Click “Record demo event” to create a sample log.")

st.markdown("---")
st.markdown("**Future hardware integration:** two IMUs → orientation estimation → personalized limits set by a qualified clinician → validated risk model → vibration feedback.")
