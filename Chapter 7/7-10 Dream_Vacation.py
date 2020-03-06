replies = {}

polling = True

while polling:
    name = input("What is your name? ")
    visit = input("What place would you like to visit? ")

    replies[name] = visit
    replies['omg'] = 'testing!!'

    again = input("Would someone else like to try? (y/n) ")
    if again == 'n':
        polling = False

print('\n---===*** Results ***===---')

for n, v in replies.items():
    print(n.title() + ' would like to visit ' + v.title() + '.')