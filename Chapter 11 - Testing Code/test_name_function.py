import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Jackie Chan' work?"""
        formatted_name = get_formatted_name('jackie', 'chan')
        self.assertEqual(formatted_name, 'Jackie Chan')


unittest.main()
