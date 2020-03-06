sandwich_orders = ['italian', 'pastrami', 'salami', 'ham']

finished_sandwiches = []

while sandwich_orders:
    building = sandwich_orders.pop()
    print(building.title() + ' sandwich being built...')
    finished_sandwiches.append(building)

print('\n***')
for finished in finished_sandwiches:
    print(finished.title() + ' completed.')