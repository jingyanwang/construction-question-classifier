from fastapi import APIRouter
from app.models.nlp_model import model

router = APIRouter()

@router.post("/predict/")
def predict(text: str):
    prediction = model.predict(text)
    return {"text": text, "prediction": prediction}
