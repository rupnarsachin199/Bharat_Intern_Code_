!pip install googletrans==4.0.0-rc1

from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    # Create a Translator object
    translator = Translator()
    
    # Translate the text
    translated_text = translator.translate(text, src=source_lang, dest=target_lang).text
    
    return translated_text

# Example usage
marathi_text = "नमस्ते"
translated_text = translate_text(marathi_text, "mr", "en")
print("Marathi text:", marathi_text)
print("Translated text:", translated_text)