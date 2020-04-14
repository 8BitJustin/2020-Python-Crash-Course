import unittest
from employee import CreateEmployee


class TestCreateEmployee(unittest.TestCase):
    """Tests for CreateEmployee class."""

    def setUp(self):
        self.new_employee = CreateEmployee('j-bone', 'saturno', 50000)
        self.default_raise_employee = self.new_employee.description()
        self.custom_raise_employee = self.new_employee.give_raise(5000)

    def test_give_default_raise(self):
        self.assertEqual(self.default_raise_employee, 'J-Bone Saturno - 50000')

    def test_give_custom_raise(self):
        self.assertEqual(self.custom_raise_employee, 'J-Bone Saturno - 55000')
