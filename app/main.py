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

@app.post("/translate/")
def translate_text(source_lang: str, target_lang: str, text: str):
    """
    Translate text from source_lang to target_lang.
    """
    try:
        result = translator.translate(source_lang, target_lang, text)
        return {"translated_text": result}
    except Exception as e:
        logging.error(f"Translation error: {str(e)}")
        raise HTTPException(status_code=500, detail="Translation failed")

# Entry point for running locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080)