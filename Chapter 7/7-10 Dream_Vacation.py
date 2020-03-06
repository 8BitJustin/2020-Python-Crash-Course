# Stores replies from input within while loop
replies = {}

polling = True

# will run as long as polling is True
while polling:
    name = input("What is your name? ")
    visit = input("What place would you like to visit? ")

    # Places 'name' as the Key and 'visit' as that key's 'value'
    replies[name] = visit

    again = input("Would someone else like to try? (y/n) ")
    if again == 'n':
        # Sets polling to False, thus killing the loop
        polling = False

print('\n---===*** Results ***===---')

for n, v in replies.items():
    print(n.title() + ' would like to visit ' + v.title() + '.')