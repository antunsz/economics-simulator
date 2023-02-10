"""
This module contains the MaritalStatus class.
"""

class MaritalStatus:
    """
    MaritalStatus class have a set of status and
    a method to set and get status
    """
    STATUS = {'single':0, 'married':0, 'divorced':0}

    def __init__(self, status: str = 'single'):
        self.set_status(status)
        self.status = status

    def get_status(self) -> str:
        return self.status

    def set_status(self, status: str):
        self.__validate_status(status)
        self.status = status

    def add_status_time(self, status: str, time: int = 1):
        self.__validate_status(status)
        self.STATUS[status] += time
    
    def __validate_status(self, status):
        if status not in self.STATUS:
            raise ValueError('The allowed status are: {}'.format(self.STATUS.keys()))

