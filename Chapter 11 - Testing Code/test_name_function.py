import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('j-bone', 'saturno')
        self.assertEqual(formatted_name, 'J-Bone Saturno')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('j-bone', 'saturno', 'richardo')
        self.assertEqual(formatted_name, 'J-Bone Richardo Saturno')
