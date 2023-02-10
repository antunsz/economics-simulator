import unittest
from src.models import Race

class TestRace(unittest.TestCase):
    def test_get_race(self):
        race = Race()
        self.assertEqual(race.get_race(), 'white')

    def test_set_race(self):
        race = Race()
        race.set_race('black')
        self.assertEqual(race.get_race(), 'black')

    def test_get_race_weight(self):
        race = Race()
        self.assertEqual(race.get_race_weight(), 70)

    def test_get_race_fat_rate(self):
        race = Race()
        self.assertEqual(race.get_race_fat_rate(), 0.1)

    def test_get_race_cancer_rate(self):
        race = Race()
        self.assertEqual(race.get_race_cancer_rate(), 0.1)

    def test_get_race_average_timelife(self):
        race = Race()
        self.assertEqual(race.get_race_average_timelife(), 80)

    def test_get_race_height(self):
        race = Race()
        self.assertEqual(race.get_race_height(), 1.70)

if __name__ == '__main__':
    unittest.main()

