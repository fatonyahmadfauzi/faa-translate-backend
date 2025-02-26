from fastapi import FastAPI
from app.services.translator import TranslatorService

app = FastAPI(title="FAA Translate Backend", version="1.0.0")

# Initialize the translator
translator = TranslatorService()

@app.get("/")
def home():
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
        return {"error": str(e)}
