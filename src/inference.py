from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc

# Load model from MLflow (latest run)
model = mlflow.pyfunc.load_model("runs:/<your_run_id>/random_forest_model")

app = FastAPI()

class Features(BaseModel):
    features: list

@app.post("/predict")
def predict(data: Features):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}
