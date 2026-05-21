import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Falcon 9 Landing Predictor", page_icon="🚀", layout="wide")
st.title("🚀 Falcon 9 First Stage Landing Predictor")

with st.sidebar:
    st.header("⚙️ API Status")
    try:
        h = requests.get(f"{API_URL}/health", timeout=3).json()
        st.success("Model loaded ✅") if h["model_loaded"] else st.warning("Model NOT loaded ⚠️")
        st.caption(h["message"])
    except Exception:
        st.error("Backend unreachable.\n```\nuvicorn main:app --reload\n```")

    st.divider()
    try:
        info = requests.get(f"{API_URL}/model-info", timeout=3).json()
        st.write(f"**Model:** {info['model_type']}")
    except Exception:
        st.caption("Model info unavailable")

with st.form("predict_form"):
    st.subheader("Launch Parameters")
    c1, c2, c3 = st.columns(3)

    with c1:
        flight_number = st.number_input("Flight Number",   min_value=1,       value=90)
        payload_mass  = st.number_input("Payload Mass (kg)", min_value=0.0, max_value=70000.0, value=5300.0, step=100.0)
        orbit         = st.selectbox("Orbit", ["LEO", "ISS", "POLAR", "SSO", "ES-L1", "HEO"])
        launch_site   = st.selectbox("Launch Site", ["KSC LC 39A", "CCAFS SLC 40", "VAFB SLC 4E"])

    with c2:
        flights      = st.number_input("Booster Flights",  min_value=0, value=2)
        block        = st.selectbox("Block Version", [1.0, 2.0, 3.0, 4.0, 5.0], index=4)
        reused_count = st.number_input("Reused Count",     min_value=0, value=1)
        serial       = st.text_input("Booster Serial", value="B1058", help="Must start with B, e.g. B1058")

    with c3:
        grid_fins   = st.checkbox("Grid Fins",     value=True)
        reused      = st.checkbox("Reused Core",   value=True)
        legs        = st.checkbox("Landing Legs",  value=True)
        landing_pad = st.text_input("Landing Pad ID (optional)", value="5e9e3032383ecb6bb234e7ca")

    submitted = st.form_submit_button("🔮 Predict", use_container_width=True, type="primary")

if submitted:
    payload = {
        "FlightNumber": flight_number,
        "PayloadMass":  payload_mass,
        "Flights":      flights,
        "Block":        block,
        "ReusedCount":  reused_count,
        "Orbit":        orbit,
        "LaunchSite":   launch_site,
        "Serial":       serial,
        "LandingPad":   landing_pad or None,
        "GridFins":     grid_fins,
        "Reused":       reused,
        "Legs":         legs,
    }

    with st.spinner("Running prediction…"):
        try:
            r = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
            r.raise_for_status()
            result = r.json()
        except requests.exceptions.ConnectionError:
            st.error("Cannot reach the FastAPI backend.")
            st.stop()
        except requests.exceptions.HTTPError:
            st.error(f"API error {r.status_code}: {r.text}")
            st.stop()

    st.divider()
    st.subheader("Result")

    rc1, rc2, rc3 = st.columns(3)
    if result["prediction"] == 1:
        rc1.success(f" {result['prediction_label']}")
    else:
        rc1.error(f" {result['prediction_label']}")

    rc2.metric("Success Probability", f"{result['probability_success']*100:.1f}%")
    rc3.metric("Failure Probability", f"{result['probability_failure']*100:.1f}%")

    st.progress(result["probability_success"], text="Confidence — successful landing")
    st.caption(f"Model: **{result['model_used']}**")

    with st.expander("Raw response"):
        st.json(result)