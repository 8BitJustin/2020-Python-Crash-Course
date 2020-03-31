from user_912 import Users


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
