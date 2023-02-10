"""
This module contains the StudyLevel class.
"""

from .StudyLevelData import STUDY_LEVELS as STUDY_LEVELS_TEMPLATE

class StudyLevel:
    """
    StudyLevel class have a set of study levels and
    a method to set and get study level
    """
    STUDY_LEVELS = {}

    def __init__(self, study_level: str = 'elementary'):
        self.study_level = None
        self.set_study_level(study_level)

    def get_study_level(self) -> str:
        return self.study_level

    def set_study_level(self, study_level: str):
        self.__validate_study_level(study_level)
        self.study_level = study_level

        if study_level not in self.STUDY_LEVELS:
            self.STUDY_LEVELS[study_level] = STUDY_LEVELS_TEMPLATE[study_level]
        
    def get_study_level_salary_impact_rate(self):
        return self.STUDY_LEVELS[self.study_level]['salary_impact_rate']

    def get_study_level_employment_rate(self):
        return self.STUDY_LEVELS[self.study_level]['employment_rate']

    def get_study_level_obsolescence_rate(self):
        return self.STUDY_LEVELS[self.study_level]['obsolescence_rate']
    
    def __validate_study_level(self, study_level):
        if study_level not in STUDY_LEVELS_TEMPLATE:
            raise ValueError(f'{study_level} not accepted.  The allowed study levels are: \
                             {STUDY_LEVELS_TEMPLATE.keys()}')
