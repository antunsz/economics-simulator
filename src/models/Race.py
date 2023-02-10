"""
This module contains a Race class.
"""

from .RaceData import RACES as RACES_TEMPLATE

class Race:
    """
    This class contains a set of races to choose 
    and a method to set and get a race
    """

    RACE = {}

    def __init__(self, race: str='white'):
        self.race = None
        self.set_race(race)

    def get_race(self) -> str:
        return self.race

    def set_race(self, race: str):
        self.__validate_race(race)
        self.race = race
        self.RACE[self.race] = RACES_TEMPLATE[self.race]

    def get_race_weight(self):
        return self.RACE[self.race]['weight']

    def get_race_fat_rate(self):
        return self.RACE[self.race]['fat_rate']

    def get_race_cancer_rate(self):
        return self.RACE[self.race]['cancer_rate']

    def get_race_average_timelife(self):
        return self.RACE[self.race]['average_timelife']

    def get_race_height(self):
        return self.RACE[self.race]['height']

    def __validate_race(self, race: str):
        if race not in RACES_TEMPLATE:
            raise ValueError(f'{race} not accepted.  The allowed races are: \
                             {RACES_TEMPLATE.keys()}')

        



