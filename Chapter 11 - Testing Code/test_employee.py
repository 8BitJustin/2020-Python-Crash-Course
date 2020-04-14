import unittest
from employee import CreateEmployee


class TestCreateEmployee(unittest.TestCase):
    """Tests for CreateEmployee class."""

    def test_give_default_raise(self):
        new_employee = CreateEmployee('j-bone', 'saturno', 50000)
        default_raise_employee = new_employee.description()
        self.assertEqual(default_raise_employee, 'J-Bone Saturno - 50000')

    def test_give_custom_raise(self):
        new_employee = CreateEmployee('j-bone', 'saturno', 50000)
        custom_raise_employee = new_employee.give_raise(5000)
        self.assertEqual(custom_raise_employee, 'J-Bone Saturno - 55000')
