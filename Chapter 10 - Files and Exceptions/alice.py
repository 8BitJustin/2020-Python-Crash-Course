filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = f"Sorry, the file: {filename} does not exist."
    print(message)
else:
    # Counts the approximate number of words in given file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {str(num_words)} words.")
