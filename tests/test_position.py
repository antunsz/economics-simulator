import unittest
from src.models import Position

class TestPosition(unittest.TestCase):
    def setUp(self):
        self.position = Position()

    def test_set_position(self):
        self.position.set_position('engineer')
        self.assertEqual(self.position.get_position(), 'engineer')

    def test_get_position(self):
        self.position.set_position('teacher')
        self.assertEqual(self.position.get_position(), 'teacher')

    def test_get_position_time(self):
        self.position.set_position('doctor')
        for i in range(40):
            self.position.add_position_time()
        self.assertEqual(self.position.get_position_time(), 40)

    def test_get_position_salary(self):
        self.position.set_position('teacher')
        self.assertEqual(self.position.get_position_salary(), 10000)

    def test_add_position_time(self):
        self.position.set_position('teacher')
        self.position.add_position_time(5)
        self.assertEqual(self.position.get_position_time(), 5)
