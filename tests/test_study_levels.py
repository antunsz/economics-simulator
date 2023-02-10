import unittest

#add the parent directory to the path
import sys
sys.path.append('..')

from src.models import StudyLevel

class TestStudyLevel(unittest.TestCase):
    def setUp(self):
        self.study_level = StudyLevel()
    
    def test_get_study_level(self):
        self.assertEqual(self.study_level.get_study_level(), 'elementary')
    
    def test_set_study_level(self):
        self.study_level.set_study_level('high_school')
        self.assertEqual(self.study_level.get_study_level(), 'high_school')
    
    def test_get_study_level_salary_impact_rate(self):
        self.assertIsInstance(self.study_level.get_study_level_salary_impact_rate(), float)
    
    def test_get_study_level_employment_rate(self):
        self.assertIsInstance(self.study_level.get_study_level_employment_rate(), float)
    
    def test_get_study_level_obsolescence_rate(self):
        self.assertIsInstance(self.study_level.get_study_level_obsolescence_rate(), float)

if __name__ == '__main__':
    unittest.main()

