filename = 'guest_book.txt'

while True:
    with open('guest_book.txt', 'a') as file_object:
        guest_name = input("Please provide your name for the guest list: ")
        message = f"We are welcome to have you attend, {guest_name.title()}!"
        file_object.write(f'{guest_name.title()} attended.\n')
        print(message)