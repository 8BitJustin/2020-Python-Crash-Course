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
        user_name = 'User: ' + self.fname.title() + ' ' + self.lname.title() \
                    + '\nLogin Attempts: ' + str(self.login_attempts)
        return user_name

    def greet_user(self):
        greeting = 'Hello, ' + self.fname.title() + ' ' + self.lname.title() \
                   + '. '
        return greeting


class Admin(Users):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = Privileges()

    def describe_admin(self):
        admin_name = self.first_name.title() + ' ' + self.last_name.title() +\
                    ', you are now an admin.'
        print(admin_name)


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('You have the following privileges:')
        for i in self.privileges:
            print('\t' + i.title())