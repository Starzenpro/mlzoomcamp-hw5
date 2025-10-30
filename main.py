from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Load the model
with open('pipeline_v1.bin', 'rb') as f:
    pipeline = pickle.load(f)

class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.get("/")
def home():
    return {"message": "Lead Scoring API"}

@app.post("/predict")
def predict(client: Client):
    client_dict = client.dict()
    probability = pipeline.predict_proba([client_dict])[0][1]
    return {"probability": probability}
