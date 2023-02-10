"""
This module contains the Age class.
"""

from datetime import date

class Age:
    """
    Age class have a born date and a mehtod
    to compute de age
    """
    def __init__(self, born_date: date = date.today()):
        self.born_date = born_date

    def get_age(self, current_year: int = date.today().year) -> int:
        return current_year - self.born_date.year



