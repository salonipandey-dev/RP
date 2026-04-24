from fastapi import FastAPI
from models import TextInput
from utils import analyze_text_logic

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ResQPaws AI running"}

@app.post("/analyze-text")
def analyze_text(data: TextInput):
    result = analyze_text_logic(data.text)
    return result