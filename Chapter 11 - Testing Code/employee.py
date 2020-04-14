class CreateEmployee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def description(self):
        print(f"First name: {self.first_name.title()}\n"
              f"Last name: {self.last_name.title()}\n"
              f"Salary: {int(self.salary)}/yr")

    def give_raise(self, increase=0):
        if increase:
            self.salary += increase
        else:
            self.salary += 5000
        return self.salary


newbie = CreateEmployee("j-bone", "saturno", 75000)

newbie.description()

newbie.give_raise()

newbie.description()

newbie.give_raise(2500)

newbie.description()
