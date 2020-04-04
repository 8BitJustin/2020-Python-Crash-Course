def count_words(filename):
    """
    Counts approximate number of words in a file.
    :param filename: Text file.
    :return: Integer - Number of words within provided text file.
    """
    try:
        with open(filename) as file_object_01:
            contents = file_object_01.read()
    except FileNotFoundError:
        # If file is missing, the file name is added to the
        # word_count_missing.txt file.
        with open('word_count_missing.txt', 'a') as file_object_02:
            file_object_02.write(f'{filename} was missing.\n')
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {int(num_words)} words.")


files = ['guest.txt', 'guest_book.txt', 'more_guests.txt', 'pi_digits.txt',
         'pie_digits.txt', 'pi_million_digits.txt', 'alice.txt']
for f in files:
    count_words(f)
