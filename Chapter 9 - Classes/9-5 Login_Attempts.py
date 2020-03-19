class Users():
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.login_attempts = 1

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 1
        return self.login_attempts

    def describe_user(self):
        user_name = 'User: ' + self.fname.title() + ' ' + self.lname.title()\
                    + '\nLogin Attempts: ' + str(self.login_attempts)
        return user_name

    def greet_user(self):
        greeting = 'Hello, ' + self.fname.title() + ' ' + self.lname.title()\
                   + '. '
        return greeting


# Creating the instance of the user class
person = Users('justin', 'olson')

# Making numerous login attempts
person.increment_login_attempts()
person.increment_login_attempts()
person.increment_login_attempts()

# Showing login attempts
print(person.describe_user())


print()

# Resetting login attempts
person.reset_login_attempts()

# Showing login attempts at reset of 0
print(person.describe_user())