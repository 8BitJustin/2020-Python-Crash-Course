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

