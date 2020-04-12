import unittest
from City_Country import city_country


class CitiesTestCase(unittest.TestCase):

    def test_cities(self):
        complete = city_country('rome', 'italy')
        self.assertEqual(complete, 'Rome, Italy')
