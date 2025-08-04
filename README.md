# FastAPI ML Service

A production-ready FastAPI-based machine learning service that provides RESTful APIs for training and predicting with machine learning models. This service is designed to handle CSV datasets and supports classification tasks using Random Forest algorithms.

## 🚀 Features

- **Model Training**: Upload CSV files and train Random Forest classification models
- **Model Prediction**: Use trained models to make predictions on new data
- **Model Management**: Automatic model persistence with unique IDs
- **RESTful API**: Clean and intuitive REST endpoints
- **Error Handling**: Comprehensive error handling and logging
- **Data Preprocessing**: Automatic handling of categorical variables and feature engineering

## 🛠️ Installation

   ```

   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

The API will be available at `http://localhost:8000`

## 🚀 Quick Start

### 1. Train a Model

```bash
doc\ -X POST "http://localhost:8000/train" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_dataset.csv" \
  -F "target_column=Survived"
```

**Response:**
```json
{
  "model_id": "00476244-000b-4516-b8aa-0eb5dcf5457d"
}
```

### 2. Make Predictions

```bash
docs\ -X POST "http://localhost:8000/predict" \
  -H "Content-Type: multipart/form-data" \
  -F "model_id=00476244-000b-4516-b8aa-0eb5dcf5457d" \
  -F "data=@test_data.csv"
```

**Response:**
```json
{
  "predictions": [
    {
      "row": 1,
      "prediction": 1,
      "meaning": "Survived"
    },
    {
      "row": 2,
      "prediction": 0,
      "meaning": "Did not Survive"
    }
  ]
}
```

## 📖 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### POST /train
Train a new machine learning model with your dataset.

**Parameters:**
- `file` (required): CSV file containing training data
- `target_column` (required): Name of the target column to predict

**Request Example:**
```bash
curl -X POST "http://localhost:8000/train" \
  -F "file=@titanic.csv" \
  -F "target_column=Survived"
```

**Response:**
```json
{
  "model_id": "uuid-string-here"
}
```

#### POST /predict
Make predictions using a trained model.

**Parameters:**
- `model_id` (required): UUID of the trained model
- `data` (required): CSV file with features for prediction

**Request Example:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -F "model_id=your-model-id" \
  -F "data=@new_data.csv"
```

**Response:**
```json
{
  "predictions": [
    {
      "row": 1,
      "prediction": 1,
      "meaning": "Survived"
    }
  ]
}
```

### Interactive API Documentation
When running the service, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

```bash
pip install -r requirements.txt
```
**Built with ❤️ using FastAPI and Scikit-learn**
