import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Dataset load karo
data = pd.read_csv("machine_data.csv")

print("Dataset Loaded Successfully!")
print(data.head())

# Features aur Target alag karo
X = data.drop("Failure", axis=1)
y = data["Failure"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model Create
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Model Train
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Model Save
joblib.dump(model, "predictive_model.pkl")

print("Model Saved as predictive_model.pkl")