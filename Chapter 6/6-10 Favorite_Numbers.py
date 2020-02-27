fav_numbers = {
    "justin": [34, 19, 10],
    "james": [15, 6, 54],
    "nick": [23, 67, 37]
}

for people, numbers in fav_numbers.items():
    print('\n' + people + ' likes the numbers: ')
    for number in numbers:
        print('\t' + str(number))