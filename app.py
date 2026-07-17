import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("predictive_model.pkl")

# Page Configuration
st.set_page_config(
    page_title="AI Predictive Maintenance System",
    page_icon="🔧",
    layout="wide"
)

# Title
st.title("🔧 AI Predictive Maintenance System")
st.write("Machine health aur maintenance risk ko AI ki madad se predict karein.")

# Sidebar
st.sidebar.header("Machine Parameters")

temperature = st.sidebar.number_input(
    "Temperature (°C)",
    min_value=0.0,
    value=65.0
)

vibration = st.sidebar.number_input(
    "Vibration",
    min_value=0.0,
    value=0.4
)

pressure = st.sidebar.number_input(
    "Pressure",
    min_value=0.0,
    value=100.0
)

rpm = st.sidebar.number_input(
    "RPM",
    min_value=0.0,
    value=1500.0
)

humidity = st.sidebar.number_input(
    "Humidity (%)",
    min_value=0.0,
    value=40.0
)

if st.sidebar.button("Predict"):

    # Input DataFrame
    input_data = pd.DataFrame({
        "Temperature": [temperature],
        "Vibration": [vibration],
        "Pressure": [pressure],
        "RPM": [rpm],
        "Humidity": [humidity]
    })

    # Prediction
    prediction = model.predict(input_data)

    # Probability
    probability = model.predict_proba(input_data)[0][1]
    probability_percent = probability * 100

    # Health Score
    health_score = 100 - probability_percent

    st.header("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        if prediction[0] == 1:
            st.error("⚠️ Maintenance Required")
        else:
            st.success("✅ Machine is Healthy")

    with col2:
        st.metric(
            "Failure Probability",
            f"{probability_percent:.2f}%"
        )

    st.metric(
        "Machine Health Score",
        f"{health_score:.2f}%"
    )

    # Progress Bars
    st.subheader("Machine Status")

    st.write("Failure Probability")
    st.progress(int(probability_percent))

    st.write("Health Score")
    st.progress(int(health_score))

    # Recommendations
    st.subheader("🔧 Maintenance Recommendations")

    recommendations = []

    if temperature > 80:
        recommendations.append(
            "🌡️ High Temperature detected. Cooling system aur fan inspect karein."
        )

    if vibration > 1.0:
        recommendations.append(
            "📳 High Vibration detected. Bearing aur shaft alignment check karein."
        )

    if pressure > 120:
        recommendations.append(
            "⚙️ High Pressure detected. Pressure valves inspect karein."
        )

    if rpm > 2400:
        recommendations.append(
            "🔄 High RPM detected. Motor calibration aur load condition check karein."
        )

    if humidity > 50:
        recommendations.append(
            "💧 High Humidity detected. Moisture protection check karein."
        )

    if len(recommendations) == 0:
        st.success(
            "✅ Sabhi parameters normal range me hain."
        )
    else:
        for recommendation in recommendations:
            st.warning(recommendation)

    # Prediction History
    history_data = {
        "Temperature": temperature,
        "Vibration": vibration,
        "Pressure": pressure,
        "RPM": rpm,
        "Humidity": humidity,
        "Failure Probability (%)": round(
            probability_percent,
            2
        ),
        "Health Score (%)": round(
            health_score,
            2
        )
    }

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append(history_data)

    st.subheader("📋 Prediction History")

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

    # Graph
    st.subheader("📈 Machine Health Trend")

    chart_data = history_df[
        [
            "Failure Probability (%)",
            "Health Score (%)"
        ]
    ]

    st.line_chart(chart_data)