

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pickle
import pandas as pd
import os

app = FastAPI()

# Enable CORS for all domains (development purpose)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model loading
with open("final_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

# Serve index.html from templates folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

@app.get("/", response_class=HTMLResponse)
async def index():
    try:
        with open(INDEX_FILE, "r") as f:
            return f.read()
    except Exception as e:
        return f"<h2>❌ Error loading index.html: {e}</h2>"

class InputData(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

@app.post("/predict")
async def predict(data: InputData):
    try:
        input_df = pd.DataFrame([data.dict()])
        prediction = model.predict(input_df)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
