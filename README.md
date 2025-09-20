text
# Bank Note Authentication

## Description
This project authenticates banknotes as genuine or counterfeit using machine learning. It analyzes features like variance, skewness, curtosis, and entropy through a Random Forest classifier. The backend API is built with FastAPI, serving predictions, while the frontend is a simple HTML/JS page served from the backend.

## Features
- Real-time banknote authenticity classification
- FastAPI backend serving REST API and frontend
- Model serialization using pickle
- CORS enabled for cross-origin requests
- Easy deployment on Render.com and similar platforms

# use this in Render : 
Set start command as:
uvicorn app:app --host 0.0.0.0 --port $PORT

text
4. Access your live app via the provided URL.

# Live demo :
You see this project Live : https://bank-note-authentication-3.onrender.com

Feel free to contribute or report issues to improve this project.
