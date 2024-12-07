from deep_translator import GoogleTranslator

class TranslatorService:
    def __init__(self, source_text, target_language):
        self.source_text = source_text
        self.target_language = target_language

    def translate(self):
        """Translate the source text to the target language."""
        return GoogleTranslator(source='auto', target=self.target_language).translate(self.source_text)
