class Users():
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def describe_user(self):
        user_name = 'User: ' + self.fname.title() + ' ' + self.lname.title()
        return user_name

    def greet_user(self):
        greeting = 'Hello, ' + self.fname.title() + ' ' + self.lname.title() + '. '
        return greeting


person_one = Users('justin', 'olson')
print(person_one.describe_user())
print(person_one.greet_user())

print()

person_two = Users('james', 'olson')
print(person_two.describe_user())
print(person_two.greet_user())

print()

person_three = Users('nick', 'olson')
print(person_three.describe_user())
print(person_three.greet_user())