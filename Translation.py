from google.cloud import translate_v2 as translate

class Translator:
    def __init__(self, credentials):
        """
        Initializes the Translator with the provided Google Cloud credentials.
        
        Args:
            credentials: Google service account Credentials object.
        """
        self.client = translate.Client(credentials=credentials)

    def translate_text(self, text: str, target_language: str) -> str:
        """
        Translates the given text into the target language using Google Cloud Translation API.
        
        Args:
            text: The input string to translate.
            target_language: The language code for the target language (e.g., 'fr' for French).
        
        Returns:
            The translated text as a string.
        """
        translation_result = self.client.translate(text, target_language=target_language)
        return translation_result.get('translatedText', '')
