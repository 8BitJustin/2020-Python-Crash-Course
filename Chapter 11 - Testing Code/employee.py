class CreateEmployee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def description(self):
        return f"{self.first_name.title()} " \
               f"{self.last_name.title()} - " \
               f"{self.salary}"

    def give_raise(self, increase=0):
        if increase:
            self.salary += increase
        else:
            self.salary += 5000
        return f"{self.first_name.title()} " \
               f"{self.last_name.title()} - " \
               f"{self.salary}"


# newbie = CreateEmployee("j-bone", "saturno", 75000)
#
# print(newbie.description())

# newbie.give_raise()
#
# newbie.description()
#
# newbie.give_raise(2500)
#
# newbie.description()
