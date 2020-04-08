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


def number_give():
    fav_num = number_retrieve()
    if fav_num:
    #     continue here
    with open(filename, 'w') as file_object:
        number = input("What is your favorite number? ")
        json.dump(number, file_object)


number_retrieve()