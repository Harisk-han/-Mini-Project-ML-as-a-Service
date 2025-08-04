
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import joblib

def train_model(df: pd.DataFrame, target_column: str, model_path: str):
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X = pd.get_dummies(X)
    if y.dtype == 'object':
        y = LabelEncoder().fit_transform(y)

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump({
        "model": model,
        "columns": X.columns.tolist()
    }, model_path)
