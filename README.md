Crop Yield Prediction using Machine Learning
 Problem Statement
Agricultural productivity is essential for food security and economic growth, but farmers often lack reliable tools to forecast crop yield based on environmental and input factors. This project aims to develop a machine learning model that predicts crop yield (in hectograms per hectare) using environmental and agricultural features.

 Solution Overview
This project uses a trained regression model to predict crop yield based on:
•	Average Rainfall
•	Average Temperature
•	Pesticide Usage
•	Area under cultivation
•	Crop Type (encoded as integers)
•	Year
The model is deployed as a FastAPI application and can accept user input via a web form.

 Technologies Used
•	Python 3
•	Machine Learning: scikit-learn (Random Forest, Gradient Boosting, etc.)
•	API: FastAPI
•	Frontend: HTML + CSS (custom web form)
•	Model Serialization: pickle
•	Deployment Ready
 Dataset
The dataset includes agricultural statistics like:
•	Rainfall
•	Temperature
•	Crop types
•	Area harvested
•	Yield in hectograms per hectare
Dataset source:Kaggle
 How It Works
1.	User inputs values in the web form:
o	Rainfall (mm)
o	Temperature (°C)
o	Pesticide used (tons)
o	Area (hectares)
o	Crop type (integer encoded)
o	Year
2.	The input is sent to the FastAPI backend via a POST request.
3.	The backend loads the trained model and returns the predicted yield in hg/ha.
4.	The result is displayed on the web page dynamically.



📂 Project Structure
├── crop_model.pkl              # Trained ML model
├── main.py                     # FastAPI backend
├── static/
│   └── index.html              # Frontend form
│   └── style.css               # Styling for the form
├── README.md                   # This file

 Run Locally
Step 1: Clone the repo
git clone https://github.com/yourusername/crop-yield-predictor.git
cd crop-yield-predictor
Step 2: Install dependenciespip install fastapi uvicorn numpy scikit-learn
Step 3: Start the server
uvicorn main:app --reload
Step 4: Open your browser
http://127.0.0.1:8000/



🙋‍♀️ About Me
I'm Janviere Uwera, a Computer and Software Engineering student passionate about data-driven solutions. I built this project as part of my journey into real-world machine learning and API deployment.
Connect with me
LinkedIn: https://www.linkedin.com/in/janviere-uwera/


