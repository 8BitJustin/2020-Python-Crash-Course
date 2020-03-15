class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        return self.name.title() + ' serves the best ' + self.cuisine + \
               ' food in town.'

    def open_restaurant(self):
        return self.name.title() + ' is open!'


seis = Restaurant('seis', 'mexican')
print(seis.name.title())
print(seis.cuisine)

print(seis.describe_restaurant())
print(seis.open_restaurant())