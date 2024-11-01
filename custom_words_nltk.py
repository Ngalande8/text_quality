from rapidfuzz import fuzz, process
from nltk.corpus import words

# Download the NLTK words dataset (if not already downloaded)


def load_custom_words(file_path):
    """
    Load additional words from a text file.

    Parameters:
    - file_path (str): The path to the text file containing additional words.

    Returns:
    - set: A set of additional words loaded from the text file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        custom_words = set(file.read().split())
    return custom_words

def find_potential_typos(sentence, custom_words_file, threshold=80):
    """
    Identifies potential typos in each word of a sentence by comparing against a combination of NLTK words and additional words from a text file.

    Parameters:
    - sentence (str): The sentence to check for potential typos.
    - custom_words_file (str): The path to the text file containing additional words.
    - threshold (int): The similarity threshold for considering a potential typo. Default is 80.

    Returns:
    - list: A list of tuples containing original words and potential replacements for words with typos.
    """
    # Get a list of English words from NLTK
    nltk_words = set(words.words())

    # Load additional words from the custom text file
    custom_words = load_custom_words(custom_words_file)

    # Combine NLTK words with custom words
    all_words = nltk_words.union(custom_words)

    # Split the sentence into individual words
    words_in_sentence = sentence.split()

    # Identify potential typos for each word
    potential_typos = []
    for word in words_in_sentence:
        match, _, score = process.extractOne(word, all_words, scorer=fuzz.ratio)
        if score < threshold:
            potential_typos.append((word, match))

    return potential_typos

# Example usage:
sentence = "I wan to learn about tx deduc"
custom_words_file = "input_file.txt"
potential_typos = find_potential_typos(sentence, custom_words_file)
if potential_typos:
    print("Potential Typos:")
    for original, replacement in potential_typos:
        print(f"- {original}: Did you mean {replacement}?")
else:
    print("No potential typos found.")
