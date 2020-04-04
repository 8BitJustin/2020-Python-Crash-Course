file_name = 'programming_poll.txt'

while True:
    with open(file_name, 'a') as f_obj:
        name = input("What is your name? ")
        response = input("Why do you like programming? ")
        f_obj.write(f'User\'s name: {name.title()}\n'
                    f'Why do you like programming? {response}\n\n')
