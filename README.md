# 🔧 AI Predictive Maintenance System

An AI-powered Predictive Maintenance System built using Machine Learning and Streamlit to predict machine failures before they happen.

## 📌 Project Overview

Unexpected machine failures can cause production delays and financial losses in industries. This project uses Machine Learning to analyze machine sensor data and predict whether maintenance is required or not.

The system also provides:
- Failure Probability
- Machine Health Score
- Maintenance Recommendations
- Prediction History
- Health Trend Visualization

---

## 🚀 Features

✅ Machine Failure Prediction  
✅ Failure Probability (%)  
✅ Machine Health Score (%)  
✅ Maintenance Recommendations  
✅ Prediction History Table  
✅ Health Trend Graph  
✅ Interactive Streamlit Dashboard  

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Joblib
- Random Forest Classifier

---

## 📂 Project Structure

```text
AI-Predictive-Maintenance-System/
│
├── app.py
├── train_model.py
├── predict.py
├── machine_data.csv
├── predictive_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/MrDIVYANSHU-0007/AI-Predictive-Maintenance-System.git
```

Move into the project directory:

```bash
cd AI-Predictive-Maintenance-System
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows
```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📊 Example Input

| Parameter | Value |
|----------|-------|
| Temperature | 85 |
| Vibration | 1.2 |
| Pressure | 125 |
| RPM | 2500 |
| Humidity | 50 |

### Output

- ⚠️ Maintenance Required
- Failure Probability: 85%
- Health Score: 15%
- Maintenance Recommendations

---

## 🎯 Future Improvements

- Real IoT Sensor Integration
- Email Alerts
- Cloud Deployment
- Advanced Visualization Dashboard
- Real Industrial Dataset Integration

---

## 👨‍💻 Author

**Divyanshu**  
B.Tech CSE (AI & ML) Student  
Babu Banarasi Das University, Lucknow

GitHub:  
https://github.com/MrDIVYANSHU-0007

---

## ⭐ If you like this project, consider giving it a star!