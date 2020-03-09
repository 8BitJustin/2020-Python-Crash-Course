def sammich_toppings(*toppings):
    print('To be added to sammich...')
    for topping in toppings:
        print('- ' + topping)


sammich_toppings('salami', 'pepperjack', 'spicy mustard')