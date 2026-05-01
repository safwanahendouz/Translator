class Translator:
    def __init__(self, language):
        self.language = language

    def translate(self, text):
        if self.language == "Spanish":
            return self.translate_to_spanish(text)
        elif self.language == "French":
            return self.translate_to_french(text)
        else:
            raise ValueError("Unsupported language")

    def translate_to_spanish(self, text):
        # Placeholder for actual translation logic
        return f"Translated to Spanish: {text}"

    def translate_to_french(self, text):
        # Placeholder for actual translation logic
        return f"Translated to French: {text}"