import string
import gradio as gr
import nltk
from nltk.corpus import brown



# Predefined path to the text file containing words to remove
TEXT_FILE_PATH = "tax_words.txt"

# Load the Brown Corpus and words to remove once, globally
BROWN_CORPUS_SET = set(brown.words())
WORDS_TO_REMOVE = set(line.strip().lower() for line in open(TEXT_FILE_PATH, 'r'))



def remove_punctuation(text):
    punctuation_table = str.maketrans('', '', string.punctuation)
    text_without_punctuation = text.translate(punctuation_table)
    return text_without_punctuation

def remove_words_from_sentence(sentence, words_to_remove):
    """
    Remove specified words from a sentence.

    Parameters:
    - sentence (str): The input sentence.
    - words_to_remove (set): Set of words to remove.

    Returns:
    - str: Sentence with specified words removed.
    """
    words = sentence.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    return ' '.join(filtered_words)

def check_for_typos(reference_set, target):
    """
    Check for potential typos in individual words of a sentence against a reference set.

    Parameters:
    - reference_set (set): Set of reference words.
    - target (str): The target string to check for typos.

    Returns:
    - str: A formatted string of words that are potential typos.
    """
    target_words = target.split()
    typos = [word for word in target_words if word.lower() not in reference_set]
    return ', '.join(typos) if typos else "No potential typos found."

def process_input(sentence):
    """
    Process the input sentence and identify potential typos.

    Parameters:
    - sentence (str): The input sentence.

    Returns:
    - (str, str): Processed sentence and formatted string of potential typos.
    """
    # Remove specified words from the sentence
    without_punctuation = remove_punctuation(sentence)
    filtered_sentence = remove_words_from_sentence(without_punctuation, WORDS_TO_REMOVE)

    # Check for typos in the filtered sentence
    typos = check_for_typos(BROWN_CORPUS_SET, filtered_sentence)

    return filtered_sentence, typos

# Setting up Gradio interface
interface = gr.Interface(
    fn=process_input,
    inputs=gr.Textbox(label="Enter your sentence:"),
    outputs=[
        gr.Textbox(label="Processed Sentence"),
        gr.Textbox(label="Potential Typos")
    ],
    title="Zax Spell Checker",
    description="Remove specified words from a sentence and check for potential typos."
)

# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch(share=True)
