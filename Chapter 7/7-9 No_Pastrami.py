sandwich_orders = ['italian', 'pastrami', 'salami', 'pastrami', 'ham',
                   'pastrami']

finished_sandwiches = []

print('We are unfortunately out of Pastrami.')

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        print('Pastrami unavailable.')
        sandwich_orders.remove('pastrami')
    building = sandwich_orders.pop()
    print(building.title() + ' sandwich being built...')
    finished_sandwiches.append(building)

print('\n***')
for finished in finished_sandwiches:
    print(finished.title() + ' completed.')