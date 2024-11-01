import nltk
from nltk.corpus import words
from rapidfuzz import process

class TypoHandler:
    def __init__(self):
        nltk.download('words')  # Download the words dataset if not already downloaded
        self.word_list = set(words.words())

    def correct_typo(self, user_input):
        corrected_words = []

        for word in user_input.split():
            result = process.extractOne(word, self.word_list)
            closest_match = result[0]
            score = result[1]

            # You can set a threshold for similarity to consider a match
            if score >= 80:
                corrected_words.append(closest_match)
            else:
                corrected_words.append(word)

        corrected_sentence = ' '.join(corrected_words)
        return corrected_sentence

# Example usage:
typo_handler = TypoHandler()

user_input = input("Enter your tax-related query: ")
corrected_input = typo_handler.correct_typo(user_input.lower())  # Convert to lowercase for case-insensitive matching

print(f"Corrected input: {corrected_input}")
# Now you can use the corrected_input in your tax chatbot processing
