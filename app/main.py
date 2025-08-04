
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from uuid import uuid4
import os
import pandas as pd
from app.utils.trainer import train_model
from app.models.model_manager import predict_with_model
import logging

app = FastAPI()

os.makedirs("app/logs", exist_ok=True)
logging.basicConfig(filename="app/logs/app.log", level=logging.INFO)

@app.post("/train")
async def train(file: UploadFile = File(...), target_column: str = Form(...)):
    try:
        df = pd.read_csv(file.file)
        if target_column not in df.columns:
            raise HTTPException(status_code=400, detail="Invalid target column")

        model_id = str(uuid4())
        model_path = f"app/storage/{model_id}.joblib"
        os.makedirs("app/storage", exist_ok=True)
        train_model(df, target_column, model_path)
        logging.info(f"Model {model_id} trained successfully.")
        return {"model_id": model_id}
    except Exception as e:
        logging.error(f"Training failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict")
async def predict(model_id: str = Form(...), data: UploadFile = File(...)):
    try:
        df = pd.read_csv(data.file)
        model_path = f"app/storage/{model_id}.joblib"
        predictions = predict_with_model(model_path, df)
        return JSONResponse(content={"predictions": predictions})
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Model ID not found")
    except Exception as e:
        logging.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
