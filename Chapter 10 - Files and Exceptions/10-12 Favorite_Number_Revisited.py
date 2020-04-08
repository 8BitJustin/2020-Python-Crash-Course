import json


def number_retrieve():
    filename = 'my_favorite_number.json'

    try:
        with open(filename) as file_object:
            fav_num = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return fav_num


def number_display():
    fav_num = number_retrieve()
    if fav_num:
        print(f"Your favorite number is {fav_num}!")
    else:
        number = input("What is your favorite number? ")
        filename = 'my_favorite_number.json'
        with open(filename, 'w') as file_object:
            json.dump(number, file_object)


number_display()
