class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        return self.name.title() + ' serves the best ' + self.cuisine + \
               ' food in town.'

    def open_restaurant(self):
        return self.name.title() + ' is open!'


taco_bell = Restaurant('taco bell', 'mexican')
mr_ans = Restaurant('mr. ans', 'asian')
dove_mt_brewery = Restaurant('dove mt. brewery', 'american')

print(taco_bell.describe_restaurant())
print(mr_ans.describe_restaurant())
print(dove_mt_brewery.describe_restaurant())