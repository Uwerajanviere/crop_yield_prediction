#  Crop Yield Prediction using Machine Learning

<p align="center">
  <img src="form-screenshot.png" alt="Web Form Screenshot" width="600"/>
</p>

##  Problem Statement
Agricultural productivity is vital for food security and economic stability. However, farmers often lack reliable tools to predict crop yield based on environmental and input factors.

 This project builds a machine learning model to predict **crop yield (in hectograms per hectare)** using agricultural and environmental data.

---

##  Solution Overview
The model predicts crop yield using:
- 🌧️ Average Rainfall (mm)
- 🌡️ Average Temperature (°C)
- 🧪 Pesticide Usage (tons)
- 🌱 Area under cultivation (hectares)
- 🌾 Crop Type (encoded as integers)
- 📅 Year

The model is deployed using **FastAPI** and can be accessed via a custom **HTML form**.

---

## 🛠️ Technologies Used
- **Python 3**
- **Machine Learning**: `scikit-learn` (Random Forest, Gradient Boosting)
- **API**: `FastAPI`
- **Frontend**: HTML + CSS
- **Serialization**: `pickle`
- **Deployment Ready**

---

## 📊 Dataset
The dataset includes:
- Rainfall  
- Temperature  
- Crop types  
- Area harvested  
- Yield (hg/ha)

> **Source**: [Crop Production Dataset – Kaggle]

---

##  How It Works
1. User enters inputs in the web form:
    - Rainfall, Temperature, Pesticides, Area, Crop Type, Year
2. Form sends data to **FastAPI** via a POST request.
3. FastAPI loads the trained model and returns the **predicted crop yield**.
4. Result is shown dynamically on the web page.

---

##  Screenshot

Here’s how the web form looks:

![Web Form Screenshot](form-screenshot1.png)
![Web Form Screenshot](form-screenshot2.png)



---

##  Run Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/crop-yield-predictor.git
cd crop-yield-predictor

# Install dependencies
pip install fastapi uvicorn scikit-learn numpy

# Run the FastAPI server
uvicorn main:app --reload
