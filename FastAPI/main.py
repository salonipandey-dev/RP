from fastapi import FastAPI
from models import TextInput
from utils import analyze_text_logic
from fastapi import File, UploadFile
from cv_utils import detect_image
import shutil
from models import SeverityInput
from utils import predict_severity_logic


app = FastAPI()

@app.get("/")
def home():
    return {"message": "ResQPaws AI running"}

@app.post("/analyze-text")
def analyze_text(data: TextInput):
    result = analyze_text_logic(data.text)
    return result

@app.post("/analyze-image")
def analyze_image(file:UploadFile=File(...)):
    file_path = file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results=detect_image(file_path)
    return {"detections": results}

@app.post("/predict-severity")
def predict_severity(data: SeverityInput):
    result = predict_severity_logic(
        data.text,
        data.image_confidence
    )
    return result