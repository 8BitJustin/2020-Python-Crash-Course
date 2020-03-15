class Users():
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def describe_user(self):
        return 'User: ' + self.fname.title() + ' ' + self.lname.title()

    def greet_user(self):
        return 'Hello, ' + self.fname.title() + ' ' + self.lname.title() + '.'


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