"""
Using your latest Restaurant class, store it in a module. Make a separate
file that imports Restaurant. Make a Restaurant instance, and call one of
Restaurant's methods to show that the import statement is working properly.
"""

import restaurant_module

tasty_noms = restaurant_module.Restaurant('chipotle', 'mexican')
print(tasty_noms.describe_restaurant())