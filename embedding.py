import spacy
import spacy_universal_sentence_encoder

#from preprocess_using_nltk import lemmatize, remove_stopwords



#nlp = spacy_universal_sentence_encoder.load_model('en_core_web_sm')

# Load the spaCy model with Universal Sentence Encoder



nlp = spacy.load('en_use_md')

# Function to calculate cosine similarity between two document vectors
def cosine_similarity(doc1, doc2):
    return doc1.vector.dot(doc2.vector) / (doc1.vector_norm * doc2.vector_norm)

# Read sentences from the text file
file_path = 'output.txt'  # Replace 'sentences.txt' with the path to your text file
with open(file_path, 'r', encoding='utf-8') as file:
    sentences = file.readlines()

# Get the input sentence
my_sentence = "tax"
#input_sentence = lemmatize(my_sentence)


# Tokenize the input sentence
doc_input = nlp(my_sentence)

# Initialize a list to store similarity scores along with corresponding sentences
similarity_scores = []

# Calculate the cosine similarity between the input sentence and each sentence from the file
for idx, sentence in enumerate(sentences, start=1):
    doc_n = nlp(sentence)
    similarity = cosine_similarity(doc_input, doc_n)
    similarity_scores.append((similarity, sentence))

# Sort the similarity scores in descending order
similarity_scores.sort(reverse=True)
#print(input_sentence)
# Print the top three pairs with the highest similarity scores
print("Top three pairs with the highest similarity scores:")
for idx, (score, sentence) in enumerate(similarity_scores[:3], start=1):
    print(f"Pair {idx}: Similarity Score: {score}, Sentence: {sentence}")
