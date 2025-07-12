from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import numpy as np
import pickle
import os
import requests

# --- Auto-download model from Google Drive if not present ---
MODEL_PATH = "crop_model.pkl"
MODEL_URL = "https://drive.google.com/uc?export=download&id=1uzUgFnp7GR1DvcXFJHB95gzxtgI-qn_E"

if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    try:
        response = requests.get(MODEL_URL)
        response.raise_for_status()
        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)
        print("Model download complete.")
    except Exception as e:
        print("Error downloading the model:", e)

# --- Load the trained model ---
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# --- Initialize FastAPI app ---
app = FastAPI()

# CORS middleware (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domain in production
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
