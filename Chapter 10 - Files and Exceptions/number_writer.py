import json

numbers = [2, 3, 5, 7, 11, 13]

# Dumps numbers list into numbers.json file.
filename = 'numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

# Loads numbers list from numbers.json file.
with open(filename) as f_obj_1:
    load_numbers = json.load(f_obj_1)

print(load_numbers)