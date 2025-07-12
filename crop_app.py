from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import numpy as np
import pickle

# Load the trained model
with open("crop_model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()

# CORS middleware (optional, for frontend API calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the web form at the root URL
@app.get("/")
def serve_form():
    return FileResponse("static/index.html")

# Prediction route
@app.post("/predict")
def predict_yield(
    avg_rainfall: float = Form(...),
    pesticides: float = Form(...),
    avg_temp: float = Form(...),
    area: int = Form(...),
    item: int = Form(...),
    year: int = Form(...)
):
    """
    Takes in form data and returns predicted crop yield.
    """
    features = np.array([[avg_rainfall, pesticides, avg_temp, area, item, year]])
    prediction = model.predict(features)[0]
    return {"predicted_yield_hg_per_ha": round(prediction, 2)}
