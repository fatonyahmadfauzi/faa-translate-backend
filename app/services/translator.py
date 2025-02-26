import os
from transformers import MarianMTModel, MarianTokenizer, M2M100ForConditionalGeneration, M2M100Tokenizer

class TranslatorService:
    def __init__(self):
        # Cache model dan tokenizer untuk efisiensi
        self.models = {}

    def get_model(self, source_lang: str, target_lang: str):
        """
        Ambil model MarianMT atau M2M100 berdasarkan environment variable.
        """
        model_name = os.getenv("MODEL_NAME", "facebook/m2m100_418M")  # Default ke model M2M100 kecil
        if model_name.startswith("facebook/m2m100"):
            if model_name not in self.models:
                self.models[model_name] = {
                    "model": M2M100ForConditionalGeneration.from_pretrained(model_name),
                    "tokenizer": M2M100Tokenizer.from_pretrained(model_name),
                }
            tokenizer = self.models[model_name]["tokenizer"]
            tokenizer.src_lang = source_lang
            tokenizer.tgt_lang = target_lang
            return self.models[model_name]
        else:
            # Gunakan MarianMT
            model_full_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
            if model_full_name not in self.models:
                self.models[model_full_name] = {
                    "model": MarianMTModel.from_pretrained(model_full_name),
                    "tokenizer": MarianTokenizer.from_pretrained(model_full_name),
                }
            return self.models[model_full_name]

    def translate(self, source_lang: str, target_lang: str, text: str) -> str:
        """
        Terjemahkan teks menggunakan model yang sesuai.
        """
        model_data = self.get_model(source_lang, target_lang)
        tokenizer = model_data["tokenizer"]
        model = model_data["model"]

        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated_tokens = model.generate(**inputs)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        return translated_text
