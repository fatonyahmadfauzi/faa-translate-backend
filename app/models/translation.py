from pydantic import BaseModel

class TranslationRequest(BaseModel):
    source_lang: str
    target_lang: str
    text: str

class TranslationResponse(BaseModel):
    translated_text: str
