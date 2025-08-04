
import joblib
import pandas as pd
def predict_with_model(model_path: str, data: pd.DataFrame):
    model_dict = joblib.load(model_path)
    model = model_dict["model"]
    expected_cols = model_dict["columns"]

    data = pd.get_dummies(data)
    for col in expected_cols:
        if col not in data.columns:
            data[col] = 0
    data = data[expected_cols]

    preds = model.predict(data)

    # Add interpretation
    interpreted = []
    for idx, p in enumerate(preds):
        meaning = "Survived" if p == 1 else "Did not Survive"
        interpreted.append({
            "row": idx + 1,
            "prediction": int(p),
            "meaning": meaning
        })
    return interpreted

