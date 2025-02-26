from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models.translation import TranslationRequest, TranslationResponse
from app.services.translator import TranslatorService
import os

# Inisialisasi FastAPI
app = FastAPI(title="FAA Translate Backend", version="1.0.0")

# Middleware CORS
allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inisialisasi layanan translator
translator = TranslatorService()

@app.get("/")
def home():
    return {"message": "Welcome to FAA Translate Backend!"}

@app.post("/translate/", response_model=TranslationResponse)
def translate_text(request: TranslationRequest):
    """
    Endpoint untuk menerjemahkan teks.
    """
    try:
        translated_text = translator.translate(
            source_lang=request.source_lang,
            target_lang=request.target_lang,
            text=request.text
        )
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
