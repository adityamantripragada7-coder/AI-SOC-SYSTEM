import pandas as pd

# Load dataset
def load_data():
    df = pd.read_csv("../data/logs.csv")
    print("✅ Data Loaded Successfully")
    print(df.head())
    return df

# Separate features and labels
def split_features(df):
    X = df.drop("label", axis=1)
    y = df["label"]

    print("\n✅ Features:")
    print(X.head())

    print("\n✅ Labels:")
    print(y.head())

    return X, y