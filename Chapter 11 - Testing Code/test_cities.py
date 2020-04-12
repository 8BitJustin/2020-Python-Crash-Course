import unittest
from city_country import city_country


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        complete_area = city_country('rome', 'italy')
        self.assertEqual(complete_area, 'Rome, Italy')

    def text_city_country_pop(self):
        complete_area_population = city_country('santiago', 'chile', 5000000)
        self.assertEqual(complete_area_population, 'Santiago, Chile - 5000000')
