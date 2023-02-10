"""
This module contains the Position class.
"""

from .PositionData import POSITIONS as POSITIONS_TEMPLATE

class Position:
    """
    Position class have a set of position and
    a method to set and get position
    """
    POSITIONS = {}

    def __init__(self, position: str = 'unemployed'):
        self.position = None
        self.set_position(position)

    def get_position(self) -> str:
        return self.position

    def set_position(self, position: str):
        self.__validate_position(position)
        self.position = position

        if position not in self.POSITIONS:
            self.POSITIONS[position] = POSITIONS_TEMPLATE[position]
        
    def get_position_time(self):
        return self.POSITIONS[self.position]['time']

    def get_position_salary(self):
        return self.POSITIONS[self.position]['salary']

    def add_position_time(self, time: int = 1):
        self.POSITIONS[self.position]['time'] += time
    
    def __validate_position(self, position):
        if position not in POSITIONS_TEMPLATE:
            raise ValueError(f'{position} not accepted.  The allowed positions are: \
                             {POSITIONS_TEMPLATE.keys()}')

