
"""House Price Prediction Project"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

DATA_PATH = os.path.join("data", "HousePriceData.xlsx")

def load_dataset():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset missing: {DATA_PATH}")
    return pd.read_excel(DATA_PATH)

def perform_eda(df):
    num_df = df.select_dtypes(include=["number"])
    plt.figure(figsize=(12,6))
    sns.heatmap(num_df.corr(), annot=True, fmt=".2f", cmap="BrBG")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.close()

def preprocess(df):
    if "SalePrice" in df.columns:
        df["SalePrice"] = df["SalePrice"].fillna(df["SalePrice"].mean())
    df = df.dropna()

    object_cols = df.select_dtypes(include=["object"]).columns
    if len(object_cols)>0:
        enc = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
        encoded = pd.DataFrame(enc.fit_transform(df[object_cols]))
        encoded.index = df.index
        encoded.columns = enc.get_feature_names_out()
        df = pd.concat([df.drop(columns=object_cols), encoded], axis=1)
    return df

def train(df):
    X = df.drop("SalePrice", axis=1)
    y = df["SalePrice"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    results = {}
    models = {
        "SVR": svm.SVR(),
        "RandomForest": RandomForestRegressor(n_estimators=50, random_state=42),
        "LinearRegression": LinearRegression()
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        results[name] = mean_absolute_percentage_error(y_test, pred)

    return results

def main():
    df = load_dataset()
    perform_eda(df)
    df = preprocess(df)
    results = train(df)
    for k,v in results.items():
        print(f"{k}: {v:.6f}")

if __name__ == "__main__":
    main()
