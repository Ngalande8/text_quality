import string

def remove_duplicates_and_store_lowercase(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
        # Remove all numbers using regex
        content_without_numbers = ''.join(char for char in content if not char.isdigit())
        # Remove punctuation using string.punctuation
        content_without_punctuation = ''.join(char for char in content_without_numbers if char not in string.punctuation)
        # Split the content into individual words
        words = content_without_punctuation.split()
        # Make all words lowercase
        lowercase_words = [word.lower() for word in words]
        # Remove duplicates by converting the list to a set and back to a list
        unique_words = list(set(lowercase_words))

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(unique_words))

# Example usage:
input_filename = 'output.txt'
output_filename = 'input_file.txt'
remove_duplicates_and_store_lowercase(input_filename, output_filename)
