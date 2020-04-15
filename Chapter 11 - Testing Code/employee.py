class CreateEmployee:
    """Class that creates employee."""

    def __init__(self, first_name, last_name, salary):
        """
        Three parameters required to create employee.
        :param first_name: Employee first name.
        :param last_name: Employee last name.
        :param salary: Employee salary.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def description(self):
        """
        Method that returns employee description.
        :return:  First Last - Salary
        """
        return f"{self.first_name.title()} " \
               f"{self.last_name.title()} - " \
               f"{self.salary}"

    def give_raise(self, increase=0):
        """
        Method provides raise. Defaulted to give 5000.
        :param increase: Any numerical/int value.
        :return: First Last - Salary (increased salary from initial creation).
        """
        if increase:
            self.salary += increase
        else:
            self.salary += 5000
        return f"{self.first_name.title()} " \
               f"{self.last_name.title()} - " \
               f"{self.salary}"


# Test code below:

"""Confirms CreateEmployee works."""
# newbie = CreateEmployee("j-bone", "saturno", 75000)
# print(newbie.description())

"""Confirms give_raise() method works properly per default."""
# newbie.give_raise()
# newbie.description()

"""Confirms give_raise() method works properly when value input."""
# newbie.give_raise(2500)
# newbie.description()
