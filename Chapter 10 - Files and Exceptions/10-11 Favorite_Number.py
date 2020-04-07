import json

filename = 'my_favorite_number.json'

with open(filename, 'w') as file_object:
    number = input("What is your favorite number? ")
    json.dump(number, file_object)
    print(f"Your favorite number is {number}.")

