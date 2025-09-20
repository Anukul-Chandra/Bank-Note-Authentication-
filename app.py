import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Enable CORS for all domains (development purpose)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # production এ specific origins দিবেন
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

with open("final_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
async def index():
    return {"message": "👋 Hello World, Welcome to Bank Note Authentication API"}

@app.post("/predict")
async def predict(data: InputData):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
