import unittest
from city_country import city_country


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        complete_area = city_country('rome', 'italy')
        self.assertEqual(complete_area, 'Rome, Italy')
