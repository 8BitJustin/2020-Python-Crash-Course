filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    message = f"Sorry, the file: {filename} does not exist."
    print(message)
