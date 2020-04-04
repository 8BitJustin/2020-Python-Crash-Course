filename = 'guest_book.txt'

while True:
    """
    Until program is stopped, input will keep asking for names to attend.
    
    When a name is given, it is appended to the guest_book.txt file, 
    and a message welcoming them to the event is printed.
    """
    with open('guest_book.txt', 'a') as file_object:
        guest_name = input("Please provide your name for the guest list: ")
        message = f"We are welcome to have you attend, {guest_name.title()}!"
        file_object.write(f'{guest_name.title()} attended.\n')
        print(message)