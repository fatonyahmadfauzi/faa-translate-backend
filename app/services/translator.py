from transformers import MarianMTModel, MarianTokenizer

class TranslatorService:
    def __init__(self):
        # Preload models and tokenizers as needed
        self.models = {}

    def get_model(self, source_lang: str, target_lang: str):
        """
        Load MarianMT model for English to Polish or English to Russian.
        """
        model_map = {
            ("en", "pl"): "Faizyhugging/Merian-Finetuned-kde4-en-to-pl",
            ("en", "ru"): "Helsinki-NLP/opus-mt-en-ru",
        }

        model_name = model_map.get((source_lang, target_lang))
        if not model_name:
            raise ValueError("Unsupported language pair. Only en-pl and en-ru are supported.")

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

# Contoh penggunaan
translator = TranslatorService()
translated_text = translator.translate("en", "ru", "Hello, how are you?")
print(translated_text)
