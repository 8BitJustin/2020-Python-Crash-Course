def the_words(filename):
    """
    Counts approximate number of times 'the' is stated within a file.
    :param filename: Text file.
    :return: Integer - Number of times 'the' is provided within the file.
    """
    with open(filename) as file_object_01:
        contents = file_object_01.read()

    the_words = contents.lower().count('the')
    print(f"The file {filename} states the word 'the' {the_words} times.")


files = ['alice.txt', 'monte_cristo.txt']
for f in files:
    the_words(f)
