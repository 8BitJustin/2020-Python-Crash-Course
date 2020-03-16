class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        return self.name.title() + ' serves the best ' + self.cuisine + \
               ' food in town. It has served ' + str(self.number_served) +  \
               ' people.'

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, customer):
        self.number_served += customer

    def open_restaurant(self):
        return self.name.title() + ' is open!'


restaurant_1 = Restaurant('chipotle', 'mexican')
print(restaurant_1.describe_restaurant())

print()

restaurant_1.number_served = 12
print(restaurant_1.describe_restaurant())

print()

restaurant_1.set_number_served(34)
print(restaurant_1.describe_restaurant())

print()

restaurant_1.increment_number_served(10)
print(restaurant_1.describe_restaurant())