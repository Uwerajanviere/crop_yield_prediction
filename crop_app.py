from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import numpy as np
import pickle
import os

# --- Load the trained model from local file ---
MODEL_PATH = "crop_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at path: {MODEL_PATH}")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# --- Initialize FastAPI app ---
app = FastAPI()

# CORS middleware (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the HTML form at root
@app.get("/")
def serve_form():
    return FileResponse("static/index.html")

# Prediction endpoint
@app.post("/predict")
def predict_yield(
    avg_rainfall: float = Form(...),
    pesticides: float = Form(...),
    avg_temp: float = Form(...),
    area: int = Form(...),
    item: int = Form(...),
    year: int = Form(...)
):
    features = np.array([[avg_rainfall, pesticides, avg_temp, area, item, year]])
    prediction = model.predict(features)[0]
    return {"predicted_yield_hg_per_ha": round(prediction, 2)}
