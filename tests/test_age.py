import unittest
from datetime import date
from src.models import Age

class TestAge(unittest.TestCase):
    def test_get_age(self):
        born_date = date(2000, 1, 1)
        age = Age(born_date)
        current_year = 2020
        self.assertEqual(age.get_age(current_year), 20)

        current_year = 2022
        self.assertEqual(age.get_age(current_year), 22)

    def test_get_age_without_current_year(self):
        born_date = date(2000, 1, 1)
        age = Age(born_date)
        self.assertEqual(age.get_age(), date.today().year - 2000)
