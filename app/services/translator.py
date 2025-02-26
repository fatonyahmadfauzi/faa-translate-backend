from transformers import MarianMTModel, MarianTokenizer

class TranslatorService:
    def __init__(self):
        # Preload models and tokenizers as needed
        self.models = {}

    def get_model(self, source_lang: str, target_lang: str):
        """
        Get or load the MarianMT model for the language pair.
        """
        model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
        if model_name not in self.models:
            self.models[model_name] = {
                "model": MarianMTModel.from_pretrained(model_name),
                "tokenizer": MarianTokenizer.from_pretrained(model_name),
            }
        return self.models[model_name]

    def translate(self, source_lang: str, target_lang: str, text: str) -> str:
        """
        Translate text using MarianMT.
        """
        model_data = self.get_model(source_lang, target_lang)
        tokenizer = model_data["tokenizer"]
        model = model_data["model"]

        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated_tokens = model.generate(**inputs)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        return translated_text