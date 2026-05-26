import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

print("🚀 Loading dataset...")

df = pd.read_csv("../data/logs.csv")

print("✅ Dataset:")
print(df)



X = df.drop(["label", "ip"], axis=1)
y = df["label"]

print("\n🔹 Features:")
print(X)

print("\n🔹 Labels:")
print(y)

print("\n⏳ Training model...")

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

print("✅ Model Training Complete")

joblib.dump(model, "model.pkl")

print("💾 Model saved as model.pkl")