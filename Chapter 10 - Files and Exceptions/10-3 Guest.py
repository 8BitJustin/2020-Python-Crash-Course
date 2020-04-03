filename = 'guest.txt'

with open('guest.txt', 'w') as file_object:
    file_object.write(input('Please provide your name for the guest list: '))

