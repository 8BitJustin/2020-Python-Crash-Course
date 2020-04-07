import json

filename = 'my_favorite_number.json'

with open(filename) as file_object:
    fav_num = json.load(file_object)
    print(f"Your favorite number is {fav_num}!")
