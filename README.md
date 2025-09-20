

# Bank Note Authentication System

## Description
This project authenticates banknotes as genuine or counterfeit using machine learning. It analyzes features like variance, skewness, curtosis, and entropy through a **Random Forest classifier**. The backend API is built with **FastAPI**, serving predictions, while the frontend is a simple HTML/JS page. This architecture allows for a seamless, real-time authentication process.

---

## Features
* **Real-time Authentication**: Instantly classify banknotes as genuine or counterfeit.
* **Decoupled Architecture**: Uses a FastAPI backend to serve both the API and the static frontend files.
* **Machine Learning Model**: Employs a **Random Forest classifier** for accurate predictions.
* **Model Persistence**: The trained model is serialized using **pickle** for efficient loading.
* **CORS Enabled**: The API supports **Cross-Origin Resource Sharing**, making it easy to integrate with other frontend applications.
* **Easy Deployment**: Designed for simple deployment on platforms like **Render.com**.

---

## Technologies Used
* **Backend**: Python, FastAPI, Scikit-learn, Pickle
* **Frontend**: HTML, CSS, JavaScript

---

## Deployment
This project is easily deployable on platforms like Render.com.

### **Render.com Deployment Command:**
To deploy the backend on Render, use this  as a start command :
```bash

uvicorn app:app --host 0.0.0.0 --port $PORT

 ```


# Live demo :
You see this project Live : https://bank-note-authentication-3.onrender.com

Feel free to contribute or report issues to improve this project.
