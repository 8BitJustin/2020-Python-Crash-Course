class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        return self.name.title() + ' serves the best ' + self.cuisine + \
               ' food in town.'

    def open_restaurant(self):
        return self.name.title() + ' is open!'


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def show_flavors(self):
        message = 'We serve: '
        for i in self.flavors:
            print(message + i.title())


ice_palace = IceCreamStand('NIICE', 'ice cream')
ice_palace.show_flavors()