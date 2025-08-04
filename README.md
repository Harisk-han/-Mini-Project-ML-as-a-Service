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
curl -X POST "http://localhost:8000/predict" \
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

## 📁 Project Structure

```
fastapi_ml_service/
├── README.md
├── requirements.txt
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── models/
│   │   └── model_manager.py    # Model prediction utilities
│   ├── utils/
│   │   └── trainer.py          # Model training utilities
│   ├── storage/               # Trained model storage
│   └── logs/
│       └── app.log            # Application logs
```

### Key Components

- **main.py**: FastAPI application with route definitions
- **model_manager.py**: Handles model loading and prediction logic
- **trainer.py**: Contains model training pipeline with preprocessing
- **storage/**: Directory for storing trained models (.joblib files)
- **logs/**: Application logging directory

## 💡 Usage Examples

### Example Dataset Format
Your CSV should have the following structure:
```csv
PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked,Survived
1,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S,0
2,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C,1
```

### Python Client Example
```python
import requests

# Train a model
files = {'file': open('data.csv', 'rb')}
data = {'target_column': 'target'}
response = requests.post('http://localhost:8000/train', files=files, data=data)
model_id = response.json()['model_id']

# Make predictions
files = {'data': open('test.csv', 'rb')}
data = {'model_id': model_id}
response = requests.post('http://localhost:8000/predict', files=files, data=data)
predictions = response.json()['predictions']
```

## ⚙️ Configuration

### Environment Variables
- `PORT`: Server port (default: 8000)
- `HOST`: Server host (default: 0.0.0.0)
- `LOG_LEVEL`: Logging level (default: INFO)

### Model Storage
- Models are stored in `app/storage/` as `.joblib` files
- Each model gets a unique UUID as filename
- Models include both the trained model and feature column information

## 📊 Logging

The application logs all training and prediction activities to `app/logs/app.log`. Log entries include:

- Training start/completion with model ID
- Prediction requests with model ID
- Error messages with stack traces
- Request metadata

**Log Format:**
```
2024-01-15 10:30:45,123 - INFO - Model 00476244-000b-4516-b8aa-0eb5dcf5457d trained successfully.
2024-01-15 10:31:15,456 - ERROR - Training failed: Invalid target column
```

## 📦 Dependencies

### Core Dependencies
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: Lightning-fast ASGI server
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms and tools
- **Joblib**: Lightweight pipelining and persistence
- **Python-multipart**: Form data parsing support

### Installation
```bash
pip install -r requirements.txt
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest

# Format code
black app/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support, please open an issue in the GitHub repository or contact the development team.

---

**Built with ❤️ using FastAPI and Scikit-learn**
