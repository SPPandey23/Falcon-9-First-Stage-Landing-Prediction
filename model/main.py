
import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from schema import Falcon9Input
from contextlib import asynccontextmanager

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "falcon9_model.pkl")
DATASET_PART_3_PATH = os.path.join(BASE_DIR, "Datasets", "dataset_part_3.csv")

model = None
scaler = None
expected_columns = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model, scaler, expected_columns
    
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
    else:
        raise RuntimeError(f"Model not found at {MODEL_PATH}")
    if os.path.exists(DATASET_PART_3_PATH):
        X = pd.read_csv(DATASET_PART_3_PATH)
        expected_columns = X.columns.tolist()
        
        X_train, _ = train_test_split(X, test_size=0.2, random_state=42)
        
        scaler = StandardScaler()
        scaler.fit(X_train)
    else:
        raise RuntimeError(f"Dataset not found at {DATASET_PART_3_PATH}")
        
    yield
    
    #optinal cleanup
    model = None
    scaler = None
    expected_columns = None

app = FastAPI(
    title="SpaceX Falcon 9 Landing Prediction API",
    description="API to predict if a Falcon 9 first stage will land successfully.",
    lifespan=lifespan
)

@app.post("/predict")
def predict_landing(data: Falcon9Input):
    if not model or not scaler or not expected_columns:
        raise HTTPException(status_code=500, detail="Model or scaler not loaded properly.")
        
    input_df = pd.DataFrame(0, index=[0], columns=expected_columns)
   
    input_df.at[0, "FlightNumber"] = data.FlightNumber
    input_df.at[0, "PayloadMass"] = data.PayloadMass
    input_df.at[0, "Flights"] = data.Flights
    input_df.at[0, "Block"] = data.Block
    input_df.at[0, "ReusedCount"] = data.ReusedCount
    
    
    orbit_col = f"Orbit_{data.Orbit}"
    if orbit_col in expected_columns:
        input_df.at[0, orbit_col] = 1
        
    launch_site_col = f"LaunchSite_{data.LaunchSite}"
    if launch_site_col in expected_columns:
        input_df.at[0, launch_site_col] = 1
        
    if data.LandingPad:
        landing_pad_col = f"LandingPad_{data.LandingPad}"
        if landing_pad_col in expected_columns:
            input_df.at[0, landing_pad_col] = 1
            
    serial_col = f"Serial_{data.Serial}"
    if serial_col in expected_columns:
        input_df.at[0, serial_col] = 1
        

    input_df.at[0, "GridFins_True"] = 1 if data.GridFins else 0
    input_df.at[0, "GridFins_False"] = 0 if data.GridFins else 1
    
    input_df.at[0, "Reused_True"] = 1 if data.Reused else 0
    input_df.at[0, "Reused_False"] = 0 if data.Reused else 1
    
    input_df.at[0, "Legs_True"] = 1 if data.Legs else 0
    input_df.at[0, "Legs_False"] = 0 if data.Legs else 1
    

    scaled_input = scaler.transform(input_df)
    
    prediction = model.predict(scaled_input)[0]
    probabilities = model.predict_proba(scaled_input)[0]
    
    return {
        "prediction": int(prediction),
        "prediction_label": "Success" if prediction == 1 else "Failure",
        "probability_success": float(probabilities[1]),
        "probability_failure": float(probabilities[0]),
        "model_used": "Random Forest"
    }

@app.get("/health")
def health_check():
    return {
        "model_loaded": model is not None,
        "message": "API is running and model is loaded" if model else "API running but model missing"
    }

@app.get("/model-info")
def model_info():
    if not model:
        raise HTTPException(status_code=500, detail="Model not loaded")
    return {
        "model_type": type(model).__name__
    }
