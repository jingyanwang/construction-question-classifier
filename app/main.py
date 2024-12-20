from fastapi import FastAPI
from app.routers import prediction

app = FastAPI()

app.include_router(prediction.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the NLP API"}
