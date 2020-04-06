def cats_and_dogs(filename):
    try:
        with open(filename) as file_object:
            content = file_object.read()
            print(content)
    except FileNotFoundError:
        print('File not in directory.')


cats_and_dogs('cats.txt')
cats_and_dogs('dogs.txt')
