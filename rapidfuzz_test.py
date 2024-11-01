import rapidfuzz
from nltk import word_tokenize
import nltk
import json

# Download NLTK words dataset
nltk.download('words')
nltk.download('punkt')
def load_exempted_words(json_file):
    try:
        with open(json_file, 'r') as file:
            exempted_words = json.load(file)
        return set(exempted_words)
    except FileNotFoundError:
        return set()

def check_typos(question, valid_words, exempted_words, threshold=80):
    question_tokens = word_tokenize(question.lower())
    typos_found = []

    for word in question_tokens:
        if word not in valid_words and not any(
            rapidfuzz.fuzz.partial_ratio(exempted_word, word) >= threshold 
            for exempted_word in exempted_words
        ):
            typos_found.append(word)

    return typos_found

def main():
    # Load NLTK words for additional reference
    valid_words = set(word.lower() for word in nltk.corpus.words.words())

    # Replace 'exempted_words.json' with the path to your exempted words JSON file
    exempted_words_file_path = 'tax_word_choices.json'
    exempted_words = set(load_exempted_words(exempted_words_file_path))

    user_question = input("Ask a question to the tax chatbot: ")

    typos = check_typos(user_question, valid_words, exempted_words)

    if typos:
        print("Potential typos found:")
        for user_word in typos:
            print(f"  '{user_word}'")
    else:
        print("No potential typos found. Your question is clear.")

if __name__ == "__main__":
    main()
