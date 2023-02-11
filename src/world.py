"""
This module conatins the World class. That will represent the space-time
"""
import datetime
import random
import logging

from src.models import (
    Individual,
    PositionData,
    RaceData,
    StudyLevelData,
    MaritalStatus
)

class World:
    """
    This class contains the attributes and methods
    to constrol the time, space and the environment
    for the agents inside it
    """

    def __init__(self, time: datetime.date = datetime.date.today()):
        self.time = time
        self.assets = []
        self.individuals = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def add_individual(self, individual):
        self.individuals.append(individual)

    def get_global_time(self) -> datetime.date:
        return self.time

    def get_global_time_in_days(self) -> int:
        return self.time.toordinal()

    def next_day(self, days: int = 1):
        """
        This method will add days to the global time
        and execute all daily tasks
        """
        #pay salaries
        self.__pay_individual_salaries()
        #add a day to global time
        self.time += datetime.timedelta(days=days)

    def get_available_assets(self) -> list:
        return [asset for asset in self.assets if asset.available]

    def get_assets_stats(self) -> dict:
        """
        This method will return a dict with the stats of the assets
        """
        assets_stats = {}
        for asset in self.assets:
            asset_id = asset.get_asset_id()
            if asset_id not in assets_stats:
                assets_stats[asset_id] = {
                    'total': 0,
                    'available': 0,
                    'average_price': asset.get_price(),
                    'depreciation_rate': asset.get_depreciation_rate()
                }
            assets_stats[asset_id]['total'] += 1
            assets_stats[asset_id]['average_price'] = (assets_stats[asset_id]['average_price'] + asset.get_price()) / 2
            assets_stats[asset_id]['depreciation_rate'] = asset.depreciation_rate
            if asset.available:
                assets_stats[asset_id]['available'] += 1
        return assets_stats


    def reproduce_population(self):
        """
        This method is used to reproduce the population
        """
        if not self.individuals:
            for i in range(20):
                individual = Individual(
                    position=random.choice(list(PositionData.POSITIONS)),
                    marital_status=random.choice(list(MaritalStatus.STATUS)),
                    race=random.choice(list(RaceData.RACES)),
                    study_level=random.choice(list(StudyLevelData.STUDY_LEVELS)),
                )
                logging.info(f'Created new individual: {individual}')
                self.add_individual(individual)

    def __pay_individual_salaries(self):
        """
        This method will pay the salaries to the individuals
        """
        for individual in self.individuals:
            individual.money += individual.get_position().get_salary()






