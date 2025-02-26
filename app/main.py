from fastapi import FastAPI, HTTPException
from app.services.translator import TranslatorService
import logging

# Initialize FastAPI app
app = FastAPI(title="FAA Translate Backend", version="1.0.0")

# Initialize the TranslatorService
translator = TranslatorService()

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    logging.info("Home endpoint called")
    return {"message": "Welcome to FAA Translate Backend!"}

from pydantic import BaseModel

class TranslateRequest(BaseModel):
    source_lang: str
    target_lang: str
    text: str

@app.post("/translate/")
def translate_text(request: TranslateRequest):
    try:
        result = translator.translate(request.source_lang, request.target_lang, request.text)
        return {"translated_text": result}
    except Exception as e:
        return {"error": str(e)}

# Entry point for running locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080)