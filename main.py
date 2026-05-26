import joblib
import pandas as pd

from threat_intel.intel_check import check_ip_reputation
from risk_engine.scorer import calculate_risk, get_severity

print("🚀 Starting AI SOC System...")

model = joblib.load("model/model.pkl")
df = pd.read_csv("data/logs.csv")

print("\n📊 Processing Logs...\n")

for _, row in df.iterrows():

    print("\n==============================")

    ip = row["ip"]

    features = [[
        row["failed_logins"],
        row["requests"],
        row["port_scans"]
    ]]

    prediction = model.predict(features)[0]

    print("IP:", ip)
    print("Prediction:", prediction)

    ml_score = 80 if prediction == "attack" else 20
    intel_score = check_ip_reputation(ip)

    risk = calculate_risk(ml_score, intel_score)
    severity = get_severity(risk)

    print("Risk:", risk)
    print("Severity:", severity)

    if severity != "LOW":
        print("🚨 ALERT GENERATED 🚨")