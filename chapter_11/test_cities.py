import unittest
from city_functions import format_city

class CitiesTestCase(unittest.TestCase):

    def test_format_city(self):
        name = format_city("Santiago", "Chile")
        self.assertEqual(name, "Santiago, Chile")

if __name__ == "__main__":
        unittest.main()