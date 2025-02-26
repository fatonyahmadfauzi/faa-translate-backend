import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from fastapi.middleware.cors import CORSMiddleware

# Inisialisasi FastAPI
app = FastAPI()

# Middleware CORS (agar bisa diakses dari frontend mana saja)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Bisa disesuaikan dengan domain yang diizinkan
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model & tokenizer
model_name = "facebook/nllb-200-distilled-600M"  # Gunakan model lebih ringan
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Mapping kode bahasa yang didukung
LANGUAGE_CODES = {
    "de": "deu_Latn", "en": "eng_Latn", "es": "spa_Latn",
    "fr": "fra_Latn", "id": "ind_Latn", "jp": "jpn_Jpan",
    "kr": "kor_Hang", "pl": "pol_Latn", "pt": "por_Latn",
    "ru": "rus_Cyrl", "zh": "zho_Hans"
}

# Model request
class TranslateRequest(BaseModel):
    text: str
    source: str
    target: str

@app.post("/translate")
async def translate(request: TranslateRequest):
    # Validasi kode bahasa
    if request.source not in LANGUAGE_CODES or request.target not in LANGUAGE_CODES:
        return {"error": "Unsupported language"}

    # Konversi kode bahasa ke format NLLB-200
    source_lang = LANGUAGE_CODES[request.source]
    target_lang = LANGUAGE_CODES[request.target]

    # Tokenisasi & Terjemahan
    inputs = tokenizer(request.text, return_tensors="pt", src_lang=source_lang)
    translated = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id[target_lang])
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return {"translatedText": translated_text}

@app.get("/")
def home():
    return {"message": "API is running"}

# Menjalankan server Uvicorn pada port yang diatur oleh Cloud Run
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
