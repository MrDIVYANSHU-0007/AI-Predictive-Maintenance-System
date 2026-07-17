import joblib
import pandas as pd

# Model load
model = joblib.load("predictive_model.pkl")

# Input data with column names
sample_data = pd.DataFrame({
    "Temperature": [85],
    "Vibration": [1.2],
    "Pressure": [125],
    "RPM": [2500],
    "Humidity": [50]
})

prediction = model.predict(sample_data)

if prediction[0] == 1:
    print("⚠️ Maintenance Required")
else:
    print("✅ Machine is Healthy")