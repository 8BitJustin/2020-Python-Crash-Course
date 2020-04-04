def count_words(filename):
    """
    Counts approximate number of words in a file.
    :param filename: Text file.
    :return: Integer - Number of words within provided text file.
    """
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = f"Sorry, file {filename} does not exist."
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {int(num_words)} words.")


count_words('guest_book.txt')
count_words('pi_digits.txt')
count_words('pi_million_digits.txt')

file = 'alice.txt'
count_words(file)