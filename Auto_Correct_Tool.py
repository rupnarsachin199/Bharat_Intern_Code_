!pip install textblob

from textblob import TextBlob

def correct_spelling(word):
    # Create a TextBlob object with the word
    blob = TextBlob(word)
    
    # Correct the spelling
    corrected_word = str(blob.correct())
    
    return corrected_word

# Example usage
misspelled_word = "accomodation"
corrected_word = correct_spelling(misspelled_word)
print("Misspelled word:", misspelled_word)
print("Corrected word:", corrected_word)