"""
Original instruction was to create a while loop that repeats pizza toppings.
Added toppings list that toppings are added to and are printed if requested.
"""

text = 'Please enter a pizza topping.'
text += '\nType \'list\' to list toppings.'
text += '\nType \'quit\' to quit. '

toppings = []
active = True

while active:
    message = input(text)
    toppings.append(message)
    if message == 'quit':
        break
    elif message == 'list':
        if message == 'list':
            toppings.pop()
        print(toppings)
    else:
        print('I\'d like to add ' + message + ' to my pizza.')